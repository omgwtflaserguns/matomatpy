import curses
import logging
from dependency_injector import catalog
from dependency_injector import providers
from .constants import Constants
from .config import Config
from .ui.menu import MenuForm
from .ui.colors import Colors
from .models.menu import MenuEntry


class Matomat:

    logging.basicConfig(filename=Constants.PATH_LOG_FILE,
                        format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s',
                        level=logging.DEBUG)

    def __init__(self, colors, menuform):
        self.colors = colors
        self.menuform = menuform

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

    matomat = providers.Singleton(Matomat, colors, menuform)
