import logging

class LogGen():
    @staticmethod
    def loggen():
        logging.basicConfig(filename="..\\OpenCartAutomation\\logs\\automation.log", format='%(asctime)s:%(levelname)s%(message)s', datefmt='%m/%d/%y %i:%M:')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger
