import logging
import configparser
from matomat.constants import Constants


class ConfigException (Exception):
    pass


class Config:

    _parser = None
    mongodb_uri = None
    loglevel = None

    def get_numeric_loglevel(self):
        numeric_level = getattr(logging, self.loglevel.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level: {}'.format(self.loglevel))
        return numeric_level

    def _read_config(self):
        self._parser = configparser.ConfigParser()

        try:
            self._parser.read(Constants.PATH_CONFIG_FILE)

            self.mongodb_uri = self._parser[Constants.CONFIG_SECTION_GENERAL][Constants.CONFIG_ATTRIBUTE_MONGODB_URI]

            self.loglevel = self._parser[Constants.CONFIG_SECTION_GENERAL][Constants.CONFIG_ATTRIBUTE_LOGLEVEL]

        except Exception as e:
            msg = 'Could not read Config file from {}, Config structure can be seen in example.conf'.format(Constants.PATH_CONFIG_FILE)
            raise ConfigException(msg) from e

    def __init__(self):
        self._read_config()
