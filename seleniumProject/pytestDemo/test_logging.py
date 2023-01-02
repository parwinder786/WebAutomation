import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)  #it will take the test case name

    fileHandler = logging.FileHandler('logfile.log') #give file name, parent logging , file location where file should be printed
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")  # print format, level can ve info or warning
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  #will take filehandler object (file location, logger is asking for format,

    #logger.setLevel(logging.CRITICAL) #level is set
    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.debug("A debug statement is executed")
    logger.warning("Something is in warning mode")
    logger.error("A Major error has happend")
    logger.critical("Critical issue")

#when you run, log file will be created