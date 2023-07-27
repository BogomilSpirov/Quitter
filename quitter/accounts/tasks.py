# from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from quitter import settings


UserModel = get_user_model()


# @shared_task
def send_registration_email(user_pk):
	try:
		user = UserModel.objects.get(pk=user_pk)
	except UserModel.DoesNotExist:
		return
	html_message = render_to_string(
		'email/email-greeting.html',
		{'user': user}
	)
	plain_message = strip_tags(html_message)
	send_mail(
		subject='Registration successful!',
		message=plain_message,
		html_message=html_message,
		from_email=settings.EMAIL_HOST_USER,
		recipient_list=(user.email,),
	)
