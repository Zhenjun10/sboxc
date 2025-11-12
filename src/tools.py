import json
import yaml
from urllib import request


def pretty_print(obj):
    print(json.dumps(obj, indent=2, ensure_ascii=False))


def get_proxies(url: str):
    req = request.Request(url, method='GET')
    with request.urlopen(req) as resp:
        stream = resp.read().decode("utf-8")
    return stream


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
