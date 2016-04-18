
import unittest
from matomat.matomat import Matomat
from matomat.models.menu import MenuKey
from tests.mock import MicroMock


class TestMatomat(unittest.TestCase):

    def setUp(self):
        self.sut = Matomat(None, None, None, None, None, MicroMock(user_has_right=lambda key: False), MicroMock.get_log_mock())


