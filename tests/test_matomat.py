
import unittest
from matomat.matomat import Matomat
from matomat.models.menu import MenuKey
from tests.mock import MicroMock

class TestMatomat(unittest.TestCase):

    def setUp(self):
        self.sut = Matomat(colors=None,
                           menuform=None,
                           loginform=None,
                           beveragesform=None,
                           config=None,
                           auth=None,
                           log=MicroMock.get_log_mock())


