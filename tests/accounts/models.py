from datetime import date

from django.core.exceptions import ValidationError
from django.test import TestCase

from quitter.accounts.models import QuitterUser


class QuitterUserTest(TestCase):
	VALID_USER_DATA = {
		'first_name': 'Test',
		'last_name': 'User',
		'email': 'bogi.spirov@gmail.com',
		'date_of_birth': date(2000, 1, 1),
		'gender': 'male',
		'profile_picture': '',
	}

	def test_valid_data(self):
		user = QuitterUser.objects.create(**self.VALID_USER_DATA)
		self.assertIsNotNone(user.pk)

	def test_invalid_first_name(self):
		invalid_user_data = self.VALID_USER_DATA
		invalid_user_data['first_name'] = 'i_contain_invalid_symbols{[(123)]}'
		with self.assertRaises(ValidationError):
			user = QuitterUser.objects.create(**invalid_user_data)
			user.full_clean()

	def test_invalid_last_name(self):
		invalid_user_data = self.VALID_USER_DATA
		invalid_user_data['last_name'] = 'i_contain_invalid_symbols{[(123)]}'
		with self.assertRaises(ValidationError):
			user = QuitterUser.objects.create(**invalid_user_data)
			user.full_clean()

	def test_first_name_starts_with_uppercase_letter(self):
		invalid_user_data = self.VALID_USER_DATA
		invalid_user_data['first_name'] = 'bogomil'
		with self.assertRaises(ValidationError):
			user = QuitterUser.objects.create(**invalid_user_data)
			user.full_clean()

	def test_last_name_starts_with_uppercase_letter(self):
		invalid_user_data = self.VALID_USER_DATA
		invalid_user_data['last_name'] = 'spirov'
		with self.assertRaises(ValidationError):
			user = QuitterUser.objects.create(**invalid_user_data)
			user.full_clean()
