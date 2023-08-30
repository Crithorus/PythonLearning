import inspect
import logging


class BaseClass:
    def getLogger(self):
        #   invoke logger with module/file name
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log')

        #   Example on how the logging format is set
        #   wrapped with % to be evaluated at run-time
        #   time : log level : name : actual message
        logFormat = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")

        fileHandler.setFormatter(logFormat)

        #   Where the log messages will be outputted
        logger.addHandler(fileHandler)  # filehandler object

        #   Set logging level (ignores everything below that level)
        logger.setLevel(logging.DEBUG)

        return logger
