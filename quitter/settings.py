"""
Django settings for quitter project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1+k8$n=#n)x41ptkn3_7(z@*sg)3i=*)284*-nb%r&n0hap%0m'  # os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # bool(int(os.getenv('DEBUG')))

ALLOWED_HOSTS = []  # os.getenv('ALLOWED_HOSTS', '').split(" ")

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'quitter.accounts.apps.AccountsConfig',
	'quitter.common',
	'quitter.quits',
	'quitter.photos',
	'fontawesomefree',
	'rest_framework'
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'quitter.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [BASE_DIR / 'templates']
		,
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

WSGI_APPLICATION = 'quitter.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'your_database_name',
#         'USER': 'your_database_user',
#         'PASSWORD': 'your_database_password',
#         'HOST': 'your_database_host',
#         'PORT': 'your_database_port',
#         'OPTIONS': {
#             'sslmode': 'require',  # Adjust this based on your PostgreSQL configuration
#         },
#     },
# }
DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.postgresql",
		"NAME": "quitter_db",
		"USER": "quitter_db_user",
		"PASSWORD": "x6vzsfjn0UxrfHhzZJ9uODE4aZGy5QN0",
		"HOST": "dpg-cldodbrmot1c73drc6e0-a.frankfurt-postgres.render.com",  # use os.getenv('DB_HOST') if production
		"PORT": "5432",
		'OPTIONS': {
            		'sslmode': 'require',  # Adjust this based on your PostgreSQL configuration
        	},
	}
}
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_URL = 'static/'
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     BASE_DIR / "static/",
# ]
STATIC_URL = '/static/'
STATICFILES_DIRS = [
	BASE_DIR / 'static',
]
STATIC_ROOT = os.getenv('STATIC_ROOT')
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'accounts.QuitterUser'
LOGIN_REDIRECT_URL = reverse_lazy('index')
LOGOUT_REDIRECT_URL = reverse_lazy('login_user')
REGISTER_REDIRECT_URL = reverse_lazy('index')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # os.getenv('EMAIL_HOST')
EMAIL_PORT = 587  # os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = True  # bool(int(os.getenv('EMAIL_USE_TLS', '1')))
EMAIL_HOST_USER = 'bogomil.spirov.quitter@gmail.com'  # os.getenv('EMAIL_HOST_USER')  # Quitter4444
EMAIL_HOST_PASSWORD = 'ckebezfhphijludz'  # os.getenv('EMAIL_HOST_PASSWORD')

# CELERY_BROKER_URL = 'redis://localhost:6379'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379'
