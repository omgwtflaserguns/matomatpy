
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

    def get_curent_user(self):
        return self.currentUser
