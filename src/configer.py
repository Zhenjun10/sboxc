from tools import *


class Configer:
    def __init__(self) -> None:
        from default_beta import config
        self.config = config

    def get_nodes_from_str(self, string):
        nodes = parse_nodes(string)
        return nodes

    def save_config(self, filename = None):
        '''保存`config`文件
        
        @param filename: 文件名，默认为 `config.json`
        @return: 无
        '''
        if filename is None:
            filename = "config.json"
        json.dump(self.config, open(f"build/{filename}", "w+", encoding="utf-8"), indent=2, ensure_ascii=False)


if __name__ == "__main__":
    cfg = Configer()
    # config.save_config()
    print(cfg.config["outbounds"])
