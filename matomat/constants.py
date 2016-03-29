import os


class Constants(object):
    CONFIG_SECTION_GENERAL = 'General'
    CONFIG_ATTRIBUTE_MONGODB_URI = 'MongoDB'

    PATH_CONFIG_FILE = os.path.expanduser('~/.matomat.conf')
    PATH_LOG_FILE = os.path.expanduser('~/matomat.log')

