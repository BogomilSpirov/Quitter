from django.test import TestCase
from django.urls import reverse


class VerificationTest(TestCase):
	VALID_USER = {
		'username': 'Bogomil0',
		'password': 'SomeStrongPassword123'
	}

	def test_login_user(self):
		self.client.login(**self.VALID_USER)
		self.client.logout()
		response = self.client.get(
			reverse('index')
		)
		self.assertEqual(200, response.status_code)


