import curses
import logging
import pyfiglet
from matomat.constants import Constants
from matomat.models.menu import MenuEntry, MenuKey
from matomat.ui.menu import MenuForm
from matomat.ui.login import LoginForm
from matomat.ui.beverages import BeveragesListForm, BeverageEditForm
from matomat.ui.colors import Colors
from matomat.services.auth import Authorization, Permissions
from matomat.services.db import Database
from matomat.services.config import Config


class Matomat:

    def __init__(self, colors, menuform, loginform, beveragesform, config, auth, log):
        self.colors = colors
        self.menuform = menuform
        self.loginform = loginform
        self.beveragesform = beveragesform
        self.config = config
        self.auth = auth
        self.screen = None
        self.log = log

    def _show_main_menu(self):
        self.menuform.set_items(self.auth.create_main_menu())
        selection = self.menuform.show(self.screen)
        self.log.debug('Menu selected Entry: %s' % selection)
        return selection

    def _login(self):
        while True:
            username, password = self.loginform.show(self.screen)
            if self.auth.login(username, password):
                break;

    def run(self, screen):
        """Runs the matomat in the given curses screen"""
        self.log.debug("-- MATOMAT START --")
        self.colors.register()
        self.screen = screen

        while True:
            self._login()

            while True:
                selection = self._show_main_menu()

                if selection == MenuKey.quit:
                    break
                elif selection == MenuKey.open_fridge:
                    pass
                elif selection == MenuKey.buy_beverage:
                    pass
                elif selection == MenuKey.manage_beverages:
                    self.beveragesform.show(self.screen)

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

        database = Database(config, log)

        auth = Authorization(database.db, log)

        menuform = MenuForm(figlet, colors)

        loginform = LoginForm(figlet, colors)

        beverageeditform = BeverageEditForm(figlet, colors, auth.db)

        beverageslistform = BeveragesListForm(figlet, colors, database.db, beverageeditform)

        matomat = Matomat(colors, menuform, loginform, beverageslistform, config, auth, log)

        curses.wrapper(matomat.run)
