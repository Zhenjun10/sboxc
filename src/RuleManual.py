class RuleManual:
    def __init__(self):
        self.DirectRules = {
            'version': 1,
            'rules': [
                {
                    'ip_cidr': [],
                    'domain': [],
                    'domain_suffix': [],
                    'domain_keyword': [],
                    'domain_regex': []
                }
            ]
        }
        self.ProxyRules = {
            'version': 1,
            'rules': [
                {
                    'ip_cidr': [],
                    'domain': [],
                    'domain_suffix': [],
                    'domain_keyword': [],
                    'domain_regex': []
                }
            ]
        }

    @property
    def direct_rules(self):
        return self.DirectRules["rules"][0]

    @property
    def proxy_rules(self):
        return self.ProxyRules["rules"][0]

    def log(self, log_type: str, string):
        if log_type == 'INFO':
            print("\033[34mINFO\033[0m", string)  # blue
        elif log_type == 'ERROR':
            print("\033[31mERROR\033[0m", string)  # red
        elif log_type == 'DONE':
            print("\033[32mDONE\033[0m", string)  # green

    def get_file_contents(self, filename: str) -> list[str]:
        import os.path
        if not os.path.exists(filename):
            self.log("ERROR", f"File not found: {filename}")
        with open(filename, "r", encoding="utf-8") as f:
            contents = f.readlines()
        return contents

    def add_custom_direct_rules(self, filename: str = None):
        if filename is None:
            filename = '.bak/custom-DirectRules'
        lines = self.get_file_contents(filename)

        for line in lines:
            if line[0] == '#':
                continue
            else:
                line = line.split()
                if line[0] == '-':
                    try:
                        self.direct_rules[line[1]].remove(line[2])
                        self.log('INFO', f"Remove {line[2]} from {line[1]} of DirectRules")
                    except:
                        self.log('ERROR', f"{line[2]} not in {line[1]} of DirectRules")
                elif line[0] == '+':
                    self.direct_rules[line[1]].append(line[2])
                    self.log('INFO', f"Add {line[2]} to {line[1]} of DirectRules")
                self.direct_rules[line[1]].sort()

    def add_custom_proxy_rules(self, filename: str = None):
        if filename is None:
            filename = '.bak/custom-ProxyRules'
        lines = self.get_file_contents(filename)

        for line in lines:
            if line[0] == '#':
                continue
            else:
                line = line.split()
                if line[0] == '-':
                    try:
                        self.proxy_rules[line[1]].remove(line[2])
                        self.log('INFO', f"Remove {line[2]} from {line[1]} of ProxyRules")
                    except:
                        self.log('ERROR',f"{line[2]} not in {line[1]} of ProxyRules")
                elif line[0] == '+':
                    self.proxy_rules[line[1]].append(line[2])
                    self.log('INFO', f"Add {line[2]} to {line[1]} of ProxyRules")
                self.proxy_rules[line[1]].sort()

    def add_custom_file_rules(self, filename: str = None):
        if filename is None:
            filename = '.bak/custom-FileRules'
        lines = self.get_file_contents(filename)

        for line in lines:
            if line[0] == "#":
                continue
            else:
                line = line.split()
                if line[0] == 'direct':
                    self.add_direct_rules(self.collect_rules(self.get_file_contents(line[1])))
                    self.log('INFO', f"Add {line[1]} to DirectRules")
                elif line[0] == 'proxy':
                    self.add_proxy_rules(self.collect_rules(self.get_file_contents(line[1])))
                    self.log('INFO', f"Add {line[1]} to ProxyRules")
                elif line[0] == 'sub':
                    self.add_direct_rules(self.collect_sub_rules(self.get_file_contents(line[1])))
                    self.log('INFO', f"Add {line[1]} to DirectRules")
                elif line[0] == 'merge':
                    direct_rules, proxy_rules = self.collect_merge_rules(self.get_file_contents(line[1]))
                    self.add_direct_rules(direct_rules)
                    self.add_proxy_rules(proxy_rules)
                    self.log('INFO', f"Add @cn to DirectRules, others to ProxyRules")

    def get_rule(self, line: str) -> tuple[str, str]:
        line = line.strip().split(":")
        length = len(line)
        if length == 1:
            return "domain_suffix", line[0]
        elif length == 2:
            if line[0] == 'full':
                return "domain", line[1]
            elif line[0] == 'regexp':
                return "domain_regex", line[1]

    def collect_rules(self, lines: list) -> dict[str, list]:
        rules = {
            "domain": [],
            "domain_suffix": [],
            "domain_regex": []
        }
        for line in lines:
            key, value = self.get_rule(line)
            rules[key].append(value)
        return rules

    def collect_sub_rules(self, lines: list):
        rules = {
            "domain": [],
        }
        for line in lines:
            line = line.strip()
            rules["domain"].append(line)
        return rules

    def collect_merge_rules(self, lines: list[str]) -> tuple[dict[str, list], dict[str, list]]:
        direct_rules = {
            "domain": [],
            "domain_suffix": [],
            "domain_regex": []
        }
        proxy_rules = {
            "domain": [],
            "domain_suffix": [],
            "domain_regex": []
        }
        for line in lines:
            if '@cn' in line:
                key, value = self.get_rule(line.replace('@cn', ''))
                direct_rules[key].append(value)
            else:
                key, value = self.get_rule(line)
                proxy_rules[key].append(value)
        return direct_rules, proxy_rules

    def add_direct_rules(self, rules: dict):
        for key in rules:
            self.direct_rules[key].extend(rules[key])
        # self.log('DONE', f"Add {filename} to DirectRules")

    def add_proxy_rules(self, rules: dict):
        for key in rules:
            self.proxy_rules[key].extend(rules[key])
        # self.log('DONE', f"Add {filename} to ProxyRules")

    def uniq_rule_files(self):
        for key in self.direct_rules:
            self.direct_rules[key] = list(set(self.direct_rules[key]))
            self.direct_rules[key].sort()
        for key in self.proxy_rules:
            self.proxy_rules[key] = list(set(self.proxy_rules[key]))
            self.proxy_rules[key].sort()
        self.log('DONE', "DirectRules and ProxyRules uniq and sort complete")

    def gen_rule_files(self):
        import json
        json.dump(self.DirectRules, open(".bak/DirectRules", "w+", encoding="utf-8"), indent=2)
        json.dump(self.ProxyRules, open(".bak/ProxyRules", "w+", encoding="utf-8"), indent=2)
        self.log('DONE', "DirectRules and ProxyRules generated")


if __name__ == "__main__":
    rm = RuleManual()
    rm.add_custom_direct_rules()
    rm.add_custom_proxy_rules()
    rm.add_custom_file_rules()
    rm.uniq_rule_files()
    rm.gen_rule_files()
