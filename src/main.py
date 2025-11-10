from configer import Configer


with open('data/subscribe', 'r', encoding='utf-8') as f:
    param = f.read()

cfg = Configer(param, "stream")
# cfg.inbounds.pop()
cfg.save_config()
