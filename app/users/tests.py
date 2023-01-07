from django.test import TestCase

from users.repository import UserRepository
from users.implemented import create_user

# Create your tests here.


class UserTestCase(TestCase):
    def setUp(self) -> None:
        self.args = {
            'name': 'Ughur',
            'surname': 'Guliyev',
            'email': 'hi@ughur.me',
            'password': 'pass1234'
        }
        self.created_user = create_user.create.run(args=self.args)

    def test_create_user(self):
        self.assertEqual(self.created_user.is_success, True)
        self.assertEqual(self.created_user.value[0].email, self.args['email'])
