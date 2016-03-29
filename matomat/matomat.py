import curses
import logging
from dependency_injector import catalog
from dependency_injector import providers
from matomat.constants import Constants
from matomat.config import Config
from matomat.ui.menu import MenuForm
from matomat.ui.colors import Colors
from matomat.models.menu import MenuEntry, MenuKey


class Matomat:

    logging.basicConfig(filename=Constants.PATH_LOG_FILE,
                        format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s',
                        level=logging.DEBUG)

    def __init__(self, colors, menuform, config):
        self.colors = colors
        self.menuform = menuform
        self.config = config
        self.screen = None

    def create_main_menu(self):
        # TODO: Build Menu from beverages and Current user permissions
        return [MenuEntry(MenuKey.buy_beverage, 'Buy ...beverage'),
                MenuEntry(MenuKey.open_fridge, 'Open Fridge'),
                MenuEntry(MenuKey.quit, 'Quit')]

    def show_main_menu(self):
        self.menuform.set_items(self.create_main_menu())
        selection = self.menuform.show(self.screen)
        logging.debug('Menu selected Entry: %s' % selection)
        return selection

    def run(self, screen):
        self.colors.register()
        self.screen = screen

        while True:
            selection = self.show_main_menu()

            if selection == MenuKey.quit:
                break;
            elif selection == MenuKey.open_fridge:
                pass
            elif selection == MenuKey.buy_beverage:
                pass

    @staticmethod
    def start():
        matomat = Catalog.matomat()
        curses.wrapper(matomat.run)


class Catalog (catalog.DeclarativeCatalog):

    config = providers.Singleton(Config)

    colors = providers.Singleton(Colors)

    menuform = providers.Singleton(MenuForm, colors)

    matomat = providers.Singleton(Matomat, colors, menuform, config)
