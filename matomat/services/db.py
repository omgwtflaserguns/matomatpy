
import logging
from pymongo import MongoClient


class DatabaseError(Exception):
    pass


class Database:

    db = None

    def __init__(self, config, log):
        self.mongodb_uri = config.mongodb_uri
        self.log = log
        self._connect()

    def _connect(self):
        try:
            self.client = MongoClient(self.mongodb_uri)
            self.log.debug('connected to mongoDB: {}'.format(self.mongodb_uri))
            self.db = self.client.matomat

        except Exception as e:
            msg = 'connection to mongoDB failed: {}'.format(self.mongodb_uri)
            self.log.fatal(msg)
            raise DatabaseError(msg) from e



