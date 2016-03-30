
import logging
from pymongo import MongoClient


class DatabaseError(Exception):
    pass


class Database:

    db = None

    def _connect(self):
        try:
            self.client = MongoClient(self.mongodb_uri)
            logging.debug('connected to mongoDB: %s' % self.mongodb_uri)
            self.db = self.client.matomat

        except Exception as e:
            msg = 'connection to mongoDB failed: %s' % self.mongodb_uri
            logging.fatal(msg)
            raise DatabaseError(msg) from e

    def __init__(self, config):
        self.mongodb_uri = config.mongodb_uri
        self._connect()
