import logging
from dependency_injector import catalog
from dependency_injector import providers
from .constants import Constants
from .config import Config


class Matomat:

    logging.basicConfig(filename=Constants.PATH_LOG_FILE, format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s', level=logging.DEBUG)

    def __init__(self, config):
        self.config = config

    def run(self):
        print(self.config.mongodb_uri)


class Catalog (catalog.DeclarativeCatalog):

    config = providers.Singleton(Config)

    matomat = providers.Singleton(Matomat, config)