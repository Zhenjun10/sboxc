from configer import Configer


SUB_URL = ''

cfg = Configer(SUB_URL)
cfg.inbounds.pop()
cfg.save_config()
