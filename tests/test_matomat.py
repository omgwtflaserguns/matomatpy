
import unittest
from matomat.matomat import Matomat
from matomat.models.menu import MenuKey


class TestMatomat(unittest.TestCase):

    def setUp(self):
        self.sut = Matomat(None, None, None, None, None)

    def test_menu_should_contain_quit(self):
        menu = self.sut.create_main_menu()
        self.assertTrue(any(item.key == MenuKey.quit for item in menu))
