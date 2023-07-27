from datetime import date
from django.test import TestCase
from quitter.accounts.models import QuitterUser
from quitter.photos.models import Photos


class PhotosTest(TestCase):
	VALID_PHOTO_DATA = {
		'name': 'PhotoPhotoPhotoPhotoPhotoPhotoPhotoPhotoPhotoPhoto',
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

	def test_all_valid_data(self):
		user = QuitterUser.objects.create(**self.VALID_USER_DATA)
		photo = Photos.objects.create(
			**self.VALID_PHOTO_DATA,
			user=user,
		)
		photo.full_clean()
		self.assertIsNotNone(photo.pk)
