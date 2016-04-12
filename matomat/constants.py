import os


class Constants(object):
    CONFIG_SECTION_GENERAL = 'General'
    CONFIG_ATTRIBUTE_MONGODB_URI = 'MongoDB'
    CONFIG_ATTRIBUTE_LOGLEVEL = 'Loglevel'

    LOG_FORMAT = '%(asctime)s %(levelname)s %(module)s %(funcName)s -> %(message)s'

    DEFAULT_LOGLEVEL = 40  # Error

    PATH_CONFIG_FILE = os.path.expanduser('~/.matomat.conf')
    PATH_LOG_FILE = os.path.expanduser('~/matomat.log')

