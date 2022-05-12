import unittest

from app.models import Comment, Pitch, User


class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username='g', password='kim')

    def test_password_setter(self):
        self.assertTrue(self.new_user.password is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('kim'))

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
        Comment.query.delete()


