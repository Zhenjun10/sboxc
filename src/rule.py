import yaml
import json
import utils


class RuleSet:
    def __init__(self):
        self.reject = {}
        self.direct = {}
        self.proxy = {}

    def get_custom_rules(self):
        with open("data/CustomRules.yml", mode="r", encoding="utf-8") as f:
            stream = f.read()
        contents = yaml.safe_load(stream)
        self.parse_custom_rules(contents)
        # print(json.dumps(contents, ensure_ascii=False, indent=2))

    def parse_custom_rules(self, contents: dict):
        for k, v in contents.items():
            if k == "reject":
                self.reject = v
            elif k == "direct":
                self.direct = v
            elif k == "proxy":
                self.proxy = v
            elif k == "url":
                self.get_url_rules(v)

    def get_url_rules(self, contents: dict):
        for k, v in contents.items():
            if k == "reject":
                self.parse_url_rules(self.reject, v)
            elif k == "direct":
                self.parse_url_rules(self.direct, v)
            elif k == "proxy":
                self.parse_url_rules(self.proxy, v)

    def parse_url_rules(self, rule_set, urls):
        for url in urls:
            stream = utils.url_get(url)
            rules = json.loads(stream).get("rules", [{}])[0]
            for key in rule_set.keys() | rules.keys():
                values = []
                for value in (rule_set.get(key), rules.get(key)):
                    if value is None:
                        continue
                    if isinstance(value, list):
                        values.extend(value)
                    else:
                        values.append(value)
                rule_set[key] = list(dict.fromkeys(values))

    def save_rule_set(self):
        rule_set = {"version": 2}
        rule_set["rules"] = [self.reject]
        json.dump(rule_set, open("build/reject.json","w",encoding="utf-8"))
        rule_set["rules"] = [self.direct]
        json.dump(rule_set, open("build/direct.json","w",encoding="utf-8"))
        rule_set["rules"] = [self.proxy]
        json.dump(rule_set, open("build/proxy.json","w",encoding="utf-8"))
