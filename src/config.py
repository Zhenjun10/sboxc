import json
import utils
from default import config
from proxy import ProxyParser


class Configer:
    def __init__(self) -> None:
        self.config = config

    def add_proxies(self):
        """给配置文件添加节点
        @param stream 节点字符串
        """
        text = self.get_sub_nodes()
        parser = ProxyParser()
        parser.parse(text)
        self.outbounds.extend(parser.proxies)
        self.manaul_select.extend(parser.tags)
        self.manaul_select.sort()
        self.auto_select.extend(parser.tags)

    def get_sub_nodes(self):
        with open('data/subscribe', 'r', encoding='utf-8') as f:
            url = f.read()
        return utils.url_get(url)

    def save_config(self, filename: str = "bin/config.json"):
        """保存config文件
        @param filename 文件名, 默认为bin/config.json
        @return 无
        """
        json.dump(
            self.config,
            open(filename, "w", encoding="utf-8"),
            indent=2,
            ensure_ascii=False,
        )
        print("保存完成！")

    @property
    def outbounds(self):
        return self.config["outbounds"]

    @property
    def manaul_select(self):
        return self.config["outbounds"][0]["outbounds"]

    @property
    def auto_select(self):
        return self.config["outbounds"][1]["outbounds"]
