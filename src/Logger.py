import time


class Logger:
    __default = "\033[0m"
    __red = "\033[31m"
    __green = "\033[32m"
    __yellow = "\033[33m"
    __blue = "\033[34m"
    __light_blue = "\033[36m"
    def __init__(self, logfile: str = None) -> None:
        self.flag = {
            "debug":   "{}[ DEBUG ]{}".format(self.__light_blue, self.__default),
            "info":    "{}[ INFO ] {}".format(self.__blue, self.__default),
            "done":    "{}[ DONE ] {}".format(self.__green, self.__default),
            "warning": "{}[WARNING]{}".format(self.__yellow, self.__default),
            "error":   "{}[ ERROR ]{}".format(self.__red, self.__default)
        }
        self.config = {
            "logfile": logfile,
            "timeformat": "default",
            "loglevel": 1
        }
    
    def debug(self, *args: str):
        self.logout(self.flag["debug"], self.concat(*args))

    def info(self, *args: str):
        self.logout(self.flag["info"], self.concat(*args))

    def done(self, *args: str):
        self.logout(self.flag["done"], self.concat(*args))

    def warning(self, *args: str):
        self.logout(self.flag["warning"], self.concat(*args))

    def error(self, *args: str):
        self.logout(self.flag["error"], self.concat(*args))

    def get_time(self):
        struct_time = time.localtime()
        # 灰色斜体
        string = "\033[3;30m{year}-{month}-{day} {hour:0>2d}:{minute:0>2d}:{second:0>2d}\033[0m".format(
            year=struct_time[0],
            month=struct_time[1],
            day=struct_time[2],
            hour=struct_time[3],
            minute=struct_time[4],
            second=struct_time[5])
        return string

    def concat(self, *args, sep=" "):
        return sep.join(args)

    def logout(self, flag: str, message: str):
        if self.config["logfile"] is None:
            print(self.get_time(), flag, message)
        ...


if __name__ == "__main__":
    logger = Logger()
    logger.debug("find a bug")
    logger.info("this", "is", "a", "apple")
    logger.done("this is done message")
    logger.warning("this is warning message")
    logger.error("error", "message")
