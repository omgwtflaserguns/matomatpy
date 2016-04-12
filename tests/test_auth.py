
import unittest
from mongobox import MongoBox
from tests.mock import MicroMock
from matomat.services.auth import Authorization


class TestAuthorization(unittest.TestCase):

    dummy_user = {'username': 'DummyUser', 'password': 'dummypassword'}

    def setUp(self):

        self.box = MongoBox()
        self.box.start()
        db = self.box.client().matomat
        db.users.insert({'username': 'DummyUser', 'password': 'dummypassword'})

        self.sut = Authorization(MicroMock(db=db), MicroMock.get_log_mock())

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
