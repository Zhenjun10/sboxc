from configer import Configer


SUB_URL = 'https://tqt-pwezahrw.tutunode.com/gateway/taoqitu?token=4bbabf8f4ca677564b30ef93778164d9'

cfg = Configer(SUB_URL)
cfg.inbounds.pop()
cfg.save_config()
