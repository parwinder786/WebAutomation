import inspect
import logging


class BaseClass:
    def getLogger(self):  # when define any method at class level, you have to defined self parameter
        loggerName = inspect.stack()[1][3] #this will give u method name, test_editProfile in child class
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger
