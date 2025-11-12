import base64
import json
import re
from tag_beautify import tag_beautifier


class URIParser:
    def __init__(self, uri):
        self.uri = uri
        self.uri_parser()

    def uri_parser(self):
        pattern = r"^(?P<protocol>\w+)://(?P<username>[\w-]+)@(?P<host>[\w.]+):(?P<port>\d+)\??(?P<params>.*?)?#(?P<tag>.*?)$"
        ret_re = re.search(pattern, self.uri).groupdict()
        if ret_re:
            self.re_parser(ret_re)
        else:
            return 1
        return 0

    def re_parser(self, ret_dict):
        self.protocol = ret_dict["protocol"]
        self.username = ret_dict["username"]
        self.host = ret_dict["host"]
        self.port = ret_dict["port"]
        if ret_dict.get("params"):
            self.param_parser(ret_dict["params"])
        self.tag = ret_dict["tag"]

    def param_parser(self, params):
        self.params = {}
        for param in params.split("&"):
            k, v = param.split("=")
            self.params[k] = v
        return 0


class ProxyParser:
    def __init__(self, stream):
        self.proxies = []
        self.servers = []
        self.tags = []
        self.proxy_parser(stream)

    def b64decode(self, string: str):
        missing_padding = (4 - len(string) % 4) % 4
        if missing_padding:
            string += "=" * missing_padding  # 补全
        return base64.b64decode(string).decode()  # 解码

    def proxy_parser(self, stream):
        lines = self.b64decode(stream).split()
        for line in lines:
            proxy = URIParser(line)
            if proxy.protocol == 'ss':
                self.ss_parser(proxy)
            elif proxy.protocol == 'trojan':
                self.trojan_parser(proxy)
            else:
                print("未解析的协议:", proxy.protocol)
        return 0

    def ss_parser(self, proxy: URIParser):
        addr = proxy.host + proxy.port
        tag = tag_beautifier(proxy.tag)
        if addr not in self.servers and tag is not None:
            self.servers.append(addr)
            method, password = self.b64decode(proxy.username).split(":")
            self.proxies.append(
                {
                    "tag": tag,
                    "type": "shadowsocks",
                    "server": proxy.host,
                    "server_port": int(proxy.port),
                    "method": method,
                    "password": password,
                }
            )
            self.tags.append(tag)
        return 0

    def vmess_parse(self, proxy: URIParser):
        content = json.loads(self.b64decode(proxy))
        addr = proxy.host + proxy.port
        tag = tag_beautifier(content["ps"])
        if addr not in self.servers and tag is not None:
            self.servers.append(addr)
            self.proxies.append({
                "tag": tag,
                "type": "vmess",
                "server": content["add"],
                "server_port": int(content["port"]),
                "uuid": content["id"],
                "security": "auto",
                "alter_id": int(content["aid"])
            })
        return 0

    def trojan_parser(self, proxy: URIParser):
        addr = proxy.host + proxy.port
        tag = tag_beautifier(proxy.tag)
        if addr not in self.servers and tag is not None:
            self.servers.append(addr)
            self.proxies.append(
                {
                    "tag": tag,
                    "type": "trojan",
                    "server": proxy.host,
                    "server_port": int(proxy.port),
                    "password": proxy.username,
                    "tls": {
                        "enabled": True,
                        "server_name": proxy.params["sni"],
                        "insecure": True if proxy.params["allowInsecure"] == '1' else False,
                        "utls": {
                            "enabled": True,
                            "fingerprint": "chrome"
                        }
                    }
                }
            )
            self.tags.append(tag)
        return 0
