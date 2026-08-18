import yaml
import base64
import requests


def url_get(url: str):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=header)
    return resp.text


def b64decode(string: str):
    missing_padding = (4 - len(string) % 4) % 4
    if missing_padding:
        string += "=" * missing_padding  # 补全
    return base64.b64decode(string).decode()  # 解码


def parse_rules(rule_sets, stream: str):
    contents = yaml.safe_load(stream)
    for k, v in contents.items():
        rule_set = {"tag": "", "type": "inline", "rules": []}
        if k == "reject":
            rule_set["tag"] = "Reject"
        elif k == "proxy":
            rule_set["tag"] = "Proxy"
        elif k == "direct":
            rule_set["tag"] = "Direct"
        rule_set["rules"].append(v)
        rule_sets.append(rule_set)
