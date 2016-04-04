
import logging


class Authorization(object):

    def __init__(self, database):
        self.db = database.db
        self.currentUser = None

    def login(self, username, password):
        user = self.db.users.find_one({'username': username, 'password': password})
        if user:
            self.currentUser = user
            logging.debug('User logged in: %s' % username)
            return True
        else:
            logging.warning('User login failed for user: %s' % username)
            return False

    def logout(self):
        if self.currentUser:
            logging.debug('User logged in: %s' % self.currentUser['username'])
        self.currentUser = None

    def user_has_right(self, key):
        if not self.currentUser:
            return False

        return key in self.currentUser['rights']


class Right:
    def __init__(self, key, name):
        self.key = key
        self.name = name


class Permissions:

    RIGHT_BUY_BEVERAGE = Right('bb', 'Buy beverage')
    RIGHT_OPEN_FRIDGE = Right('of', 'Open fridge')
    RIGHT_SHOW_STATS = Right('ss', 'Show Stats')
    RIGHT_DEPOSIT_CREDITS = Right('dc', 'Deposit Credits')
    RIGHT_SHOW_HISTORY = Right('sh', 'Show History')
    RIGHT_CHANGE_PASSWORD = Right('cp', 'Change Password')
    RIGHT_MANAGE_ACCOUNTS = Right('ma', 'Manage Accounts')
    RIGHT_MANAGE_BEVERAGES = Right('mb', 'Manage Beverages')
