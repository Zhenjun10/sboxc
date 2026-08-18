from config import Configer
from rule import RuleSet


cfg = Configer()
cfg.add_proxies()
cfg.save_config()

ruleset = RuleSet()
ruleset.get_custom_rules()
ruleset.save_rule_set()
