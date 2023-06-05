import os

from decouple import config

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'USER': os.environ['RDS_USERNAME'],
		'PASSWORD': os.environ['RDS_PASSWORD'],
		'HOST': os.environ['RDS_HOSTNAME'],
		'PORT': os.environ['RDS_PORT'],
	}
}

GOOGLE_MAP_API_KEY = config("GOOGLE_MAP_API_KEY")

AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = "production-r-bucket"
AWS_S3_REGION_NAME = 'ap-northeast-3'

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Configure media files storage
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
