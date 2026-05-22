# tag_beautify.py
import re
from urllib import parse

# ====== 区域关键字 ======
REGIONS = [
    {"keywords": ["剩余", "流量", "到期", "过期", "免费"], "zh": "信息"},
    {"keywords": ["HK", "Hong Kong", "香港"], "zh": "香港"},
    {"keywords": ["JP", "Japan", "日本", "Tokyo", "Osaka"], "zh": "日本"},
    {"keywords": ["SG", "Singapore", "新加坡"], "zh": "新加坡"},
    {"keywords": ["TW", "Taiwan", "台湾", "Taipei"], "zh": "台湾"},
    {"keywords": ["US", "USA", "United States", "美国", "Los Angeles"], "zh": "美国"},
    {"keywords": ["KR", "Korea", "韩国", "Seoul"], "zh": "韩国"},
    {"keywords": ["CN", "China", "中国", "大陆"], "zh": "中国"},
    {"keywords": ["GB", "England", "英国", "UK", "United Kingdom", "Britain"], "zh": "英国"},
    {"keywords": ["ES", "Spain", "西班牙"], "zh": "西班牙"},
    {"keywords": ["MY", "Malaysia", "马来西亚", "马来", "馬來", "MALAYSIA", "KualaLumpur"], "zh": "马来西亚"},
    {"keywords": ["CN", "Turkey", "土耳其", "TUR"], "zh": "土耳其"},
    {"keywords": ["AR", "Argentina", "阿根廷"], "zh": "阿根廷"},
    {"keywords": ["CA", "Canada", "加拿大", "楓葉", "枫叶", "CAN", "CANADA"], "zh": "加拿大"},
    {"keywords": ["DE", "德国", "德國"], "zh": "德国"},
    {"keywords": ["RU", "俄罗斯", "俄羅斯", "俄国", "俄國"], "zh": "俄罗斯"},
    {"keywords": ["IN", "印度", "India", "IND", "INDIA"], "zh": "印度"},
    {"keywords": ["AU", "澳大利亚", "Australia", "澳洲", "Sydney"], "zh": "澳大利亚"},
    {"keywords": ["FR", "法国", "France", "法國", "巴黎"], "zh": "法国"},
    {"keywords": ["UA", "乌克兰", "Ukraine", "烏克蘭", "基辅"], "zh": "乌克兰"},
]

# ====== 节点美化类 ======
class TagBeautifier:
    def __init__(self, regions=REGIONS):
        self.regions = regions
        self.counts = {}  # 每个地区编号计数

    def _find_region(self, name: str):
        name_lower = name.lower()
        for region in self.regions:
            for kw in region["keywords"]:
                if kw.lower() in name_lower:
                    return region
        return None

    def _detect_line_type(self, name: str) -> str:
        name_upper = name.upper()
        if "BGP" in name_upper:
            return "BGP"
        elif "IEPL" in name_upper:
            return "IEPL"
        elif "三网" in name_upper:
            return "三网"
        elif "HOME" in name_upper:
            return "HOME"
        else:
            return ""  # 无线路类型则返回空

    def _detect_multiplier(self, name: str) -> str:
        # 匹配倍率：x2, ×3, x3.5, X1.2等
        match = re.search(r'[x×X](\d+(?:\.\d+)?)', name)
        if match:
            return f"x{match.group(1)}"
        else:
            return "x1"  # 默认倍率

    def beautify(self, tag: str, subscription_name: str = '') -> str:
        tag = parse.unquote(tag)
        region = self._find_region(tag)

        if not region:
            return f"{subscription_name} | {tag}".strip(" |")
        elif region["zh"] == '信息':
            return None

        line_type = self._detect_line_type(tag)
        multiplier = self._detect_multiplier(tag)
        region_name = region["zh"]
        self.counts[region_name] = self.counts.get(region_name, 0) + 1
        idx = f"{self.counts[region_name]:02d}"

        # 拼接右侧部分
        right_part = f"{line_type}{multiplier}" if line_type else multiplier
        return f"{subscription_name} | {region_name} {idx} | {right_part}".strip(" |")

# ====== 模块级实例 ======
_beautifier = TagBeautifier()

def beautitag(tag: str, subscription_name: str = '') -> str:
    """每次传入一个节点名与订阅名，返回美化后的节点名称"""
    return _beautifier.beautify(tag, subscription_name)
