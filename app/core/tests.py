from django.test import TestCase

from core.implemented import create_promo_code, check_promo_code
from core.repository import promo_code_repository

# Create your tests here.

class PromoCodeCheckerTest(TestCase):
    def setUp(self) -> None:
        self.args = {
            'name': 'buca2020',
            'discount_percentage': 20,
            'limit': 2000,
            'is_active': True,
        }
        self.code = create_promo_code.create.run(args=self.args)
    
    def test_create_code(self):
        self.assertEqual(self.code.is_success, True)
        self.assertEqual(self.code.value.name, self.args['name'])
        self.assertEqual(self.code.value.is_active, self.args['is_active'])
    
    def test_check_code(self):
        checked_code = check_promo_code.check.run(name=self.code.value.name)
        self.assertEqual(checked_code.value.is_active, self.args['is_active'])

