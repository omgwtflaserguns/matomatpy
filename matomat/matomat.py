import curses
import logging
import pyfiglet
from matomat.constants import Constants
from matomat.models.menu import MenuEntry, MenuKey
from matomat.ui.menu import MenuForm
from matomat.ui.login import LoginForm
from matomat.ui.colors import Colors
from matomat.services.auth import Authorization, Permissions
from matomat.services.db import Database
from matomat.services.config import Config


class Matomat:

    def __init__(self, colors, menuform, loginform, config, auth, log):
        self.colors = colors
        self.menuform = menuform
        self.loginform = loginform
        self.config = config
        self.auth = auth
        self.screen = None
        self.log = log

    def _create_main_menu(self):
        # TODO: Build Menu from beverages and Current user permissions
        menu = []

        if self.auth.user_has_right(Permissions.RIGHT_BUY_BEVERAGE.key):
            menu.append(MenuEntry(MenuKey.buy_beverage, 'Buy ...beverage'))

        if self.auth.user_has_right(Permissions.RIGHT_OPEN_FRIDGE.key):
            menu.append(MenuEntry(MenuKey.open_fridge, 'Open Fridge'))

        menu.append(MenuEntry(MenuKey.quit, 'Quit'))

        return menu

    def _show_main_menu(self):
        self.menuform.set_items(self._create_main_menu())
        selection = self.menuform.show(self.screen)
        self.log.debug('Menu selected Entry: %s' % selection)
        return selection

    def run(self, screen):
        """Runs the matomat in the given curses screen"""
        self.log.debug("-- MATOMAT START --")
        self.colors.register()
        self.screen = screen

        while True:
            username, password = self.loginform.show(screen)
            if self.auth.login(username, password):
                break;

        while True:

            selection = self._show_main_menu()

            if selection == MenuKey.quit:
                break
            elif selection == MenuKey.open_fridge:
                pass
            elif selection == MenuKey.buy_beverage:
                pass

    @staticmethod
    def start():
        """Starts a new matomat instance"""

        colors = Colors()

        figlet = pyfiglet.Figlet()

        config = Config()

        logging.basicConfig(filename=config.logfile,
                            format=Constants.LOG_FORMAT,
                            level=config.get_numeric_loglevel())
        log = logging.getLogger()

        db = Database(config, log)

        auth = Authorization(db, log)

        menuform = MenuForm(colors, figlet)

        loginform = LoginForm(colors, figlet)

        matomat = Matomat(colors, menuform, loginform, config, auth, log)

        curses.wrapper(matomat.run)
