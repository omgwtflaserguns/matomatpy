import logging
import configparser
from matomat.constants import Constants

class Config:

    _parser = None
    mongodb_uri = None

    def __init__(self):
        self._parser = configparser.ConfigParser()
        logging.debug('Reading Config from %s' % Constants.PATH_CONFIG_FILE)
        self._parser.read(Constants.PATH_CONFIG_FILE)

        self.mongodb_uri = self._parser[Constants.CONFIG_SECTION_GENERAL][Constants.CONFIG_ATTRIBUTE_MONGODB_URI]
        logging.debug('Config - %s -> %s' % (Constants.CONFIG_ATTRIBUTE_MONGODB_URI, self.mongodb_uri))





