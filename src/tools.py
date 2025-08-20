import base64
import json
import re
import yaml
from urllib import request, parse


nodes_re = {
    "ss": re.compile(r'^(\w+)@(.*?):(\d+)#(.*?)$')
}


def b64decode(string: str):
    missing_padding = (4 - len(string) % 4) % 4  
    if missing_padding:
        string += "=" * missing_padding  # 补全
    return base64.b64decode(string).decode()  # 解码


def pretty_print(obj):
    print(json.dumps(obj, indent=2, ensure_ascii=False))


def get_nodes(url: str):
    req = request.Request(url, method='GET')
    with request.urlopen(req) as resp:
        stream = resp.read().decode("utf-8")
    return stream


def parse_nodes(stream: str):
    nodes = []
    raws = b64decode(stream).split()
    for node in raws:
        type, content = parse.unquote(node).split('://')
        if type == 'ss':
            content = nodes_re['ss'].search(content).groups() # type: ignore
            method, password = b64decode(content[0]).split(":")
            result = {
                "tag": content[3],
                "type": "shadowsocks",
                "server": content[1],
                "server_port": int(content[2]),
                "method": method,
                "password": password
            }
        elif type == 'vmess':
            content = json.loads(b64decode(content))
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


def get_rules(filename: str):
    with open(filename, mode='r', encoding='utf-8') as f:
        stream = f.read()
    return stream


def format_rules(obj, contents):
    for content in contents:
        type, item = content.split(', ')
        if obj.get(type) is None:
            obj[type] = [item]
        else:
            obj[type].append(item)


def parse_rules(stream: str):
    contents = yaml.safe_load(stream)
    rules = []
    for k, v in contents.items():
        if k == 'reject':
            rule = {"action": "reject"}
            format_rules(rule, v)
        elif k == 'proxy':
            rule = {"action": "route", "outbound": "手动选择"}
            format_rules(rule, v)
        elif k == 'direct':
            rule = {"action": "route", "outbound": "DIRECT"}
            format_rules(rule, v)
        rules.append(rule)
    return rules
