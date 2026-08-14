import json
import re
import utils
from tag import tag_beautify


class Proxy:
    def __init__(self, protocol: str):
        self.proto = protocol


class SSProxy(Proxy):
    def __init__(self, context: str):
        super().__init__("shadowsocks")
        self.context = context
        self.parse()

    def get(self):
        return {
            "tag": self.tag,
            "type": self.proto,
            "server": self.host,
            "server_port": self.port,
            "method": self.method,
            "password": self.passwd,
        }

    def v1(self):
        pattern = r"^(?P<mpwd>[\w-]+)@(?P<host>[\w.]+):(?P<port>\d+)#(?P<tag>.*?)$"
        ret = re.search(pattern, self.context).groupdict()
        self.tag = tag_beautify(ret["tag"])
        self.host = ret["host"]
        self.port = int(ret["port"])
        self.method, self.passwd = utils.b64decode(ret["mpwd"]).split(":")

    def v2(self):
        pattern = r"^(?P<meth>[\w-]+):(?P<pwd>[\w-]+)@(?P<host>[\w.-]+):(?P<port>\d+)$"
        context, tag = self.context.split("#")
        context = utils.b64decode(context)
        ret = re.search(pattern, context).groupdict()
        self.tag = tag_beautify(tag)
        self.host = ret["host"]
        self.port = int(ret["port"])
        self.method = ret["meth"]
        self.passwd = ret["pwd"]

    def parse(self):
        funcs = [self.v1, self.v2]
        for fn in funcs:
            try:
                fn()
                self.proxy = self.get()
                break
            except AttributeError:
                continue
        else:
            print("解析失败!", self.context)
            self.proxy = None


class TrojanProxy(Proxy):
    def __init__(self, context: str):
        super().__init__("trojan")
        self.context = context


class VmessProxy(Proxy):
    def __init__(self, context: str):
        super().__init__("vmess")
        self.context = context
        self.parse()

    def get(self):
        return {
            "tag": self.tag,
            "type": self.proto,
            "server": self.host,
            "server_port": self.port,
            "uuid": self.uuid,
            "security": "auto",
            "alter_id": self.aid,
        }

    def v1(self):
        ret = json.loads(utils.b64decode(self.context))
        self.tag = tag_beautify(ret["ps"])
        self.host = ret["add"]
        self.port = int(ret["port"])
        self.uuid = ret["id"]
        self.aid = int(ret["aid"])

    def parse(self):
        funcs = [self.v1]
        for fn in funcs:
            try:
                fn()
                self.proxy = self.get()
                break
            except AttributeError:
                continue
        else:
            print("解析失败!", self.context)
            self.proxy = None


class ProxyParser:
    def __init__(self, stream):
        self.proxies = []
        self.servers = []
        self.tags = []
        self.proxy_parser(stream)

    def proxy_parser(self, stream):
        lines = utils.b64decode(stream).split()
        for line in lines:
            proto, context = line.split("://")
            if proto == 'ss':
                self.unique(SSProxy(context))
            elif proto == 'trojan':
                self.unique(TrojanProxy(context))
            elif proto == 'vmess':
                self.unique(VmessProxy(context))
            else:
                print("未解析的协议:", proto)

    def unique(self, p):
        if p.proxy is not None:
            addr = p.host + str(p.port)
            if addr not in self.servers and p.tag is not None:
                self.servers.append(addr)
                self.proxies.append(p.proxy)
                self.tags.append(p.tag)
