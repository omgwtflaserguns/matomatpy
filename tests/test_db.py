
import unittest
from tests.mock import MicroMock
from matomat.services.db import Database, DatabaseError


class TestDatabase(unittest.TestCase):

    def test_should_throw_on_wrong_database_uri(self):
        with self.assertRaises(DatabaseError):
            Database(MicroMock(mongodb_uri='thereshouldbenomongoDBbehindthisuri'))
