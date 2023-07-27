from datetime import date
from django.test import TestCase
from django.urls import reverse
from quitter.accounts.models import QuitterUser
from quitter.common.forms import SearchForm, AddCommentForm
from quitter.photos.models import Photos
from quitter.quits.models import Quit


class ViewTest(TestCase):
	VALID_PHOTO_DATA = {
		'name': 'New Photo',
		'about': 'Some about info...',
		'url': 'https://upload.wikimedia.org/wikipedia/commons/b/b6/Image_created_with_a_mobile_phone.png',
	}
	VALID_USER_DATA = {
		'first_name': 'Test',
		'last_name': 'User',
		'email': 'test@test.com',
		'date_of_birth': date(2000, 1, 1),
		'gender': 'male',
		'profile_picture': '',
	}
	VALID_QUIT_DATA = {
		'title': 'New Quit',
		'photo': None,
		'description': 'some quit',
		'user': None
	}

	def setUp(self):
		user = QuitterUser.objects.create(**self.VALID_USER_DATA)
		self.VALID_QUIT_DATA['user'] = user
		self.VALID_PHOTO_DATA['user'] = user
		photo = Photos.objects.create(**self.VALID_PHOTO_DATA)
		self.VALID_QUIT_DATA['photo'] = photo
		self.quit1 = Quit.objects.create(**self.VALID_QUIT_DATA)

	def test_index_view_right_template(self):
		response = self.client.get(
			reverse('index')
		)
		self.assertEqual(200, response.status_code)
		self.assertEqual(1, len(response.context['quits']))
		self.assertTemplateUsed(response, 'common/base.html')
		self.assertEqual(200, response.status_code)

	def test_search_form(self):
		response = self.client.get(reverse('index'))
		self.assertIsInstance(response.context['search_form'], SearchForm)

	def test_comment_form(self):
		response = self.client.get(reverse('index'))
		self.assertIsInstance(response.context['comment_form'], AddCommentForm)

	def test_search_form_in_action(self):
		response = self.client.get(reverse('index'), {'search_text': 'New Quit'})
		self.assertEqual(200, response.status_code)
		self.assertEqual(1, len(response.context['quits']))
