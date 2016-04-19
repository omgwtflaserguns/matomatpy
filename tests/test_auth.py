
import unittest
from mongobox import MongoBox
from tests.mock import MicroMock
from matomat.services.auth import Authorization
from matomat.models.menu import MenuKey


class TestAuthorization(unittest.TestCase):

    dummy_user = {'username': 'DummyUser', 'password': 'dummypassword'}

    def setUp(self):

        self.box = MongoBox()
        self.box.start()
        db = self.box.client().matomat
        db.users.insert({'username': 'DummyUser', 'password': 'dummypassword'})

        self.sut = Authorization(db, MicroMock.get_log_mock())

    def tearDown(self):
        self.box.stop()

    def test_should_set_logged_in_user(self):
        self.assertTrue(self.sut.login('DummyUser', 'dummypassword'))
        self.assertTrue(set(self.dummy_user.items()).issubset(set(self.sut.currentUser.items())))

    def test_should_not_login_wrong_username(self):
        self.assertFalse(self.sut.login('wrongUser', 'dummypassword'))
        self.assertTrue(self.sut.currentUser is None)

    def test_should_not_login_wrong_password(self):
        self.assertFalse(self.sut.login('DummyUser', 'wrongPassword'))
        self.assertTrue(self.sut.currentUser is None)

    def test_main_menu_should_not_contain_prohibited_Entries(self):
        menu = self.sut.create_main_menu()
        self.assertTrue(len(menu) == 1 and menu[0].key == MenuKey.quit)

    def test_main_menu_should_contain_quit(self):
        menu = self.sut.create_main_menu()
        self.assertTrue(any(item.key == MenuKey.quit for item in menu))
