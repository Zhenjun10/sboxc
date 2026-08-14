from config import Configer


with open('data/subscribe', 'r', encoding='utf-8') as f:
    stream = f.read()

cfg = Configer(stream, "url")
cfg.save_config()
