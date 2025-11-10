import base64
import json
import re
import yaml
from urllib import request, parse
from nodebeautifier import beautify_nodes


nodes_re = {
    "ss": re.compile(r'^(\w+)@(.*?):(\d+)#(.*?)$')
}
node_addrs = []


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


def parse_ss(nodes, content):
    content = nodes_re['ss'].search(content).groups()
    addr = content[1] + content[2]
    tag = beautify_nodes(content[3])
    if addr not in node_addrs and tag is not None:
        node_addrs.append(addr)
        method, password = b64decode(content[0]).split(":")
        nodes.append({
            "tag": tag,
            "type": "shadowsocks",
            "server": content[1],
            "server_port": int(content[2]),
            "method": method,
            "password": password
        })
    else:
        tag = None
    return tag


def parse_vmess(nodes, content):
    content = json.loads(b64decode(content))
    addr = content["add"] + content["port"]
    tag = beautify_nodes(content["ps"])
    if addr not in node_addrs and tag is not None:
        node_addrs.append(addr)
        nodes.append({
            "tag": tag,
            "type": "vmess",
            "server": content["add"],
            "server_port": int(content["port"]),
            "uuid": content["id"],
            "security": "auto",
            "alter_id": int(content["aid"])
        })
    else:
        tag = None
    return tag


def parse_nodes(nodes, stream: str):
    tags = []
    raws = b64decode(stream).split()
    for node in raws:
        flag, content = parse.unquote(node).split('://')
        if flag == 'ss':
            tag = parse_ss(nodes, content)
        elif flag == 'vmess':
            tag = parse_vmess(nodes, content)
        else:
            print("未解析的协议:", flag)
            tag = None
        if tag is not None:
            tags.append(tag)
    return tags


def format_rules(obj, contents):
    for content in contents:
        type, item = content.split(', ')
        if obj.get(type) is None:
            obj[type] = [item]
        else:
            obj[type].append(item)


def parse_rules(rule_sets, stream: str):
    contents = yaml.safe_load(stream)
    for k, v in contents.items():
        rule_set = {"tag": "", "type": "inline", "rules": [{}]}
        if k == 'reject':
            rule_set["tag"] = "Reject"
            format_rules(rule_set["rules"][0], v)
        elif k == 'proxy':
            rule_set["tag"] = "Proxy"
            format_rules(rule_set["rules"][0], v)
        elif k == 'direct':
            rule_set["tag"] = "Direct"
            format_rules(rule_set["rules"][0], v)
        rule_sets.append(rule_set)
