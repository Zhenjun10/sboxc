import base64
import json
import re
from urllib import request, parse


class Converter():
    def __init__(self, url = None) -> None:
        if url is not None:
            req = request.Request(url, method='GET')
            with request.urlopen(req) as resp:
                stream = resp.read().decode("utf-8")
            self.nodes = self.parse_nodes(stream)
    
    def init_pattern(self):
        self.pattern = {
            "ss": re.compile(r'^(\w+)@(.*?):(\d+)#(.*?)$')  # 
        }

    def b64decode(self, string: str):
        missing_padding = (4 - len(string) % 4) % 4  
        if missing_padding:
            string += "=" * missing_padding  # 补全
        return base64.b64decode(string).decode()  # 解码
    
    def pretty_print(self, obj):
        print(json.dumps(obj, indent=2, ensure_ascii=False))

    def parse_nodes(self, stream: str):
        self.init_pattern()
        nodes = []
        raws = self.b64decode(stream).split()
        for node in raws:
            type, content = parse.unquote(node).split('://')
            if type == 'ss':
                content = self.pattern['ss'].search(content).groups() # type: ignore
                method, password = self.b64decode(content[0]).split(":")
                result = {
                    "tag": content[3],
                    "type": "shadowsocks",
                    "server": content[1],
                    "server_port": int(content[2]),
                    "method": method,
                    "password": password
                }
            elif type == 'vmess':
                content = json.loads(self.b64decode(content))
                result = {
                    "tag": content["ps"],
                    "type": "vmess",
                    "server": content["add"],
                    "server_port": int(content["port"]),
                    "uuid": content["id"],
                    "security": "auto",
                    "alter_id": int(content["aid"])
                }
            nodes.append(result)
        return nodes


if __name__ == "__main__":
    ...

