import json
import yaml
from converter import Converter


class Configer:
    def __init__(self) -> None:
        from default_beta import config
        self.config = config

    def get_nodes_from_str(self, string):
        convert = Converter().parse_nodes(string)
        return convert
    
    def get_nodes_from_url(self, url):
        convert = Converter(url)
        return convert.nodes

    def add_node(self):
        ...

    def save_config(self, filename = None):
        '''保存`config`文件
        
        @param filename: 文件名，默认为 `config.json`
        @return: 无
        '''
        if filename is None:
            filename = "config.json"
        json.dump(self.config, open(f"build/{filename}", "w+", encoding="utf-8"), indent=2, ensure_ascii=False)


if __name__ == "__main__":
    config = Configer()
    # config.save_config()
    print(config.config["outbounds"])
