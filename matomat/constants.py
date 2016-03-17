import os


class Paths(object):
    CONFIG_FILE = os.path.expanduser('~/.matomat.conf')

class Options(object):
    MONGODB_URI = 'MongoDB URI'

class Forms(object):

    LOGIN_FORM = 'LOGIN'
    BEVERAGE_FORM = 'BEVERAGES'
    MENU_FORM = 'MENU'
    CONFIG_FORM = 'CONFIG'
    MAIN_FORM = 'MAIN'
