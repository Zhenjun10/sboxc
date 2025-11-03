from configer import Configer


with open('data/SUB_URL', 'r', encoding='utf-8') as f:
    url = f.read()

cfg = Configer(url)
# cfg.inbounds.pop()
cfg.save_config()
