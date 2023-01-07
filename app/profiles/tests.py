from django.test import TestCase

from profiles.implemented import (
    create_business, 
    create_standard,
    create_vip,
    create_basic
)
from users.implemented import create_user

# Create your tests here.


class ProfilesTestCase(TestCase):
    def setUp(self) -> None:
        self.business_args = {
            'name': 'Business 1',
            'type': 'general',
        }
        self.standard_args = {
            'name': 'Ughur',
            'surname': 'Guliyev',
            'phone_number': '0702251511'
        }
        self.user_args = {
            'name': 'Ughur',
            'surname': 'Guliyev',
            'email': 'hi@ughur.me',
            'password': 'pass1234'
        }
        self.created_user = create_user.create.run(args=self.user_args)
        self.created_business = create_business.create.run(
            user_id=self.created_user.value[0].id, 
            args=self.business_args
        )
        self.created_standard = create_standard.create.run(
            user_id=self.created_user.value[0].id, 
            args=self.standard_args
        )
    
    def test_created_business(self):
        self.assertEqual(self.created_business.is_success, True)
        self.assertEqual(self.created_business.value.name, self.business_args['name'])
    
    def test_created_standard(self):
        self.assertEqual(self.created_standard.is_success, True)
        self.assertEqual(self.created_standard.value.phone_number, self.standard_args['phone_number'])
    
    def test_create_vip(self):
        self.created_vip = create_vip.create.run(
            user_id=self.created_user.value[0].id,
            args=self.standard_args
        )
        self.assertEqual(self.created_vip.is_success, True)
    
    def test_create_basic(self):
        self.created_basic = create_basic.create.run(user_id=self.created_user.value[0].id)
        self.assertEqual(self.created_basic.is_success, True)