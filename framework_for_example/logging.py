import http.client as http_client
import logging
import os


class Logging:
    def __init__(self):

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

        console = logging.StreamHandler()
        console.setLevel(logging.WARNING)
        console.setFormatter(formatter)

        filehandler = logging.FileHandler(os.getcwd() + '/logger.log')
        filehandler.setLevel(logging.INFO)
        filehandler.setFormatter(formatter)
        self.logger.addHandler(console)
        self.logger.addHandler(filehandler)

    def logging(self):
        http_client.HTTPConnection.debuglevel = 1
        return self.logger
