from django.test import TestCase, Client
from django.urls import reverse

from quitter.accounts.forms import RegisterUserForm


class RegisterFormTest(TestCase):
	VALID_REGISTER_USER = {
		'username': 'Bogomil0',
		'email': 'bogi.spirov@gmail.com',
		'password1': 'SomeStrongPassword123',
		'password2': 'SomeStrongPassword123',
	}

	def setUp(self):
		self.client = Client(**self.VALID_REGISTER_USER)
		self.register_url = reverse('register_user')

	def test_register_view(self):
		response = self.client.get(self.register_url)
		self.assertTemplateUsed(response, 'accounts/register.html')

	def test_register_form(self):
		response = self.client.get(self.register_url)
		self.assertIsInstance(response.context['form'], RegisterUserForm)
