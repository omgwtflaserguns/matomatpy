import curses
import logging
from dependency_injector import catalog
from dependency_injector import providers
from matomat.constants import Constants
from matomat.config import Config
from matomat.ui.menu import MenuForm
from matomat.ui.colors import Colors
from matomat.models.menu import MenuEntry


class Matomat:

    logging.basicConfig(filename=Constants.PATH_LOG_FILE,
                        format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s',
                        level=logging.DEBUG)

    def __init__(self, colors, menuform, config):
        self.colors = colors
        self.menuform = menuform
        self.config = config

    def run(self, screen):
        self.colors.register()

        self.menuform.set_items([MenuEntry('maeh', 'Buy beer'), MenuEntry('maeh', 'Buy mate'), MenuEntry('maeh', 'Do stuff')])
        self.menuform.show(screen)

    @staticmethod
    def start():
        matomat = Catalog.matomat()
        curses.wrapper(matomat.run)


class Catalog (catalog.DeclarativeCatalog):

    config = providers.Singleton(Config)

    colors = providers.Singleton(Colors)

    menuform = providers.Singleton(MenuForm, colors)

    matomat = providers.Singleton(Matomat, colors, menuform, config)
