
from matomat.models.menu import MenuKey, MenuEntry


class Authorization(object):

    def __init__(self, db, log):
        self.db = db
        self.currentUser = None
        self.log = log

    def login(self, username, password):
        """Try to login the given username and password combination, returns wether login was successful"""
        user = self.db.users.find_one({'username': username, 'password': password})
        if user:
            self.currentUser = user
            self.log.debug('User logged in: {}'.format(username))
            return True
        else:
            self.log.warning('User login failed for user: {}'.format(username))
            return False

    def logout(self):
        """Logout the current logged-in user"""
        if self.currentUser:
            self.log.debug('User logged out: {}'.format(self.currentUser['username']))
        self.currentUser = None

    def user_has_right(self, key):
        """Returns wether or not the currently logged in user has the right to the given key"""
        if not self.currentUser:
            return False

        return key in self.currentUser['rights']

    def create_main_menu(self):
        # TODO: Build Menu from beverages and Current user permissions
        menu = []

        if self.user_has_right(Permissions.RIGHT_BUY_BEVERAGE.key):
            pass

        if self.user_has_right(Permissions.RIGHT_OPEN_FRIDGE.key):
            menu.append(MenuEntry(MenuKey.open_fridge, 'Open Fridge'))

        if self.user_has_right(Permissions.RIGHT_MANAGE_BEVERAGES.key):
            menu.append(MenuEntry(MenuKey.manage_beverages, 'Manage beverages'))

        menu.append(MenuEntry(MenuKey.quit, 'Quit'))

        return menu


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
