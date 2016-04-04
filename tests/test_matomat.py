
import unittest
from matomat.matomat import Matomat
from matomat.models.menu import MenuKey
from tests.mock import MicroMock


class TestMatomat(unittest.TestCase):

    def setUp(self):
        self.sut = Matomat(None, None, None, None, MicroMock(user_has_right=lambda key: False))

    def test_main_menu_should_not_contain_prohibited_Entries(self):
        menu = self.sut._create_main_menu()
        self.assertTrue(len(menu) == 1 and menu[0].key == MenuKey.quit)

    def test_main_menu_should_contain_quit(self):
        menu = self.sut._create_main_menu()
        self.assertTrue(any(item.key == MenuKey.quit for item in menu))
