import logging


#   Example of logging in pytest

def test_logging():
    #   invoke logger with module/file name
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')

    #   Example on how the logging format is set
    #   wrapped with % to be evaluated at run-time
    #   time : log level : name : actual message
    logFormat = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")

    fileHandler.setFormatter(logFormat)

    #   Where the log messages will be outputted
    logger.addHandler(fileHandler)  # filehandler object

    #   Set logging level (ignores everything below that level)
    logger.setLevel(logging.INFO)

    #   Examples of logging types: debug, info, warning, error,  critical...
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("something is in warning mode")
    logger.error("A major error has occured")
    logger.critical("Critical Issue")
