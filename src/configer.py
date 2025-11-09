import json
import tools
from default import config


class Configer:
    def __init__(self, param: str, flag: str) -> None:
        '''初始化

        @param param: 参数, 可以是网址 (URL), 也可以是字符串 (stream)
        @param flag: 标识`param`的类型, 可填`url`, `stream`
        '''
        self.config = config
        self.set_nodes(param, flag)
        self.set_rules()

    def set_nodes(self, param: str, flag: str):
        '''给配置文件添加节点

        @param param: 参数, 可以是网址 (URL), 也可以是字符串 (stream)
        @param flag: 标识`param`的类型, 可填`url`, `stream`
        '''
        if flag == 'url':
            stream = tools.get_nodes(param)
        elif flag == 'stream':
            stream = param
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
