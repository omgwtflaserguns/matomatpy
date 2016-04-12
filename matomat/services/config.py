import logging
import configparser
from matomat.constants import Constants


class ConfigException (Exception):
    pass


class Config:

    _parser = None
    mongodb_uri = None
    loglevel = None

    def __init__(self):
        self._parser = configparser.ConfigParser()
        logging.debug('Reading Config from %s' % Constants.PATH_CONFIG_FILE)

        try:
            self._parser.read(Constants.PATH_CONFIG_FILE)

            self.mongodb_uri = self._parser[Constants.CONFIG_SECTION_GENERAL][Constants.CONFIG_ATTRIBUTE_MONGODB_URI]
            logging.debug('Config - %s -> %s' % (Constants.CONFIG_ATTRIBUTE_MONGODB_URI, self.mongodb_uri))

            self.loglevel = self._parser[Constants.CONFIG_SECTION_GENERAL][Constants.CONFIG_ATTRIBUTE_LOGLEVEL]
            logging.debug('Config - %s -> %s' % (Constants.CONFIG_ATTRIBUTE_LOGLEVEL, self.loglevel))

        except Exception as e:
            msg = 'Could not read Config file from %s Config structure can be seen in example.conf' % Constants.PATH_CONFIG_FILE
            logging.fatal(msg)
            raise ConfigException(msg) from e
