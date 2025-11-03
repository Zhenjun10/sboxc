import json
import tools
from default import config


class Configer:
    def __init__(self, url: str) -> None:
        self.config = config
        self.set_nodes(url)
        self.set_rules()

    def set_nodes(self, url: str):
        stream = tools.get_nodes(url)
        tags = tools.parse_nodes(self.outbounds, stream)
        self.manaul.extend(tags)
        self.auto.extend(tags)

    def save_config(self, filename: str = 'build/config.json'):
        '''保存`config`文件
        
        @param filename: 文件名，默认为 `build/config.json`
        @return: 无
        '''
        json.dump(self.config, open(filename, "w+", encoding="utf-8"), indent=2, ensure_ascii=False)
        print("保存完成！")

    @property
    def inbounds(self):
        return self.config["inbounds"]

    @property
    def outbounds(self):
        return self.config["outbounds"]

    @property
    def manaul(self):
        return self.config["outbounds"][0]["outbounds"]
    
    @property
    def auto(self):
        return self.config["outbounds"][1]["outbounds"]
    
    @property
    def rule_set(self):
        return self.config["route"]["rule_set"]
    
    def set_rules(self):
        with open('src/CustomRules.yml', mode='r', encoding='utf-8') as f:
            stream = f.read()
        tools.parse_rules(self.rule_set, stream)
