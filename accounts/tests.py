from django.test import TestCase
from accounts.models import Accounts

class AccountsTestCase (TestCase):

	def test_check_account(self):
		Act = Accounts()
		self.assertEqual(Act.CheckAccount(), True)

