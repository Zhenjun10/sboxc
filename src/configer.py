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
    def rules(self):
        return self.config["route"]["rules"]
    
    def set_rules(self):
        with open('src/CustomRules.yml', mode='r', encoding='utf-8') as f:
            stream = f.read()
        tools.parse_rules(self.rules, stream)


if __name__ == "__main__":
    cfg = Configer("https://tqt-pwezahrw.tutunode.com/gateway/taoqitu?token=4bbabf8f4ca677564b30ef93778164d9")
    # tools.pretty_print(cfg.manaul)
    # tools.pretty_print(cfg.auto)
    # tools.pretty_print(cfg.outbounds)
    # tools.pretty_print(cfg.rules)
    cfg.inbounds.pop()
    cfg.save_config()
