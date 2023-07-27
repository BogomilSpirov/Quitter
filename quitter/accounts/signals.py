from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_registration_email

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def created_user(instance, created, **kwargs):
	if created:
		send_registration_email(instance.pk)
