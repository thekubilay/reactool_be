from decouple import config
from reactool_be.settings import BASE_DIR

# CSRF_TRUSTED_ORIGINS = []

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'development',
		'USER': 'kubilay',
		'PASSWORD': 'WMAwQ6ZQJ',
		'HOST': 'development.czcvrhueuznd.ap-northeast-3.rds.amazonaws.com',
		'PORT': '5432',
	}
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [
	BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

STORAGES = {
	'staticfiles': {
		'BACKEND': 'storages.backends.s3boto3.S3Boto3Storage',
		'BUCKET': 'development-r-bucket',
		'LOCATION': 'static',
	},
	'media': {
		'BACKEND': 'storages.backends.s3boto3.S3Boto3Storage',
		'BUCKET': 'development-r-bucket',
		'LOCATION': 'media',
	}
}

AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = "development-r-bucket"
AWS_S3_REGION_NAME = 'ap-northeast-3'

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_FILE_OVERWRITE = True

# MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com/media/'

EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)

GOOGLE_MAP_API_KEY = config("GOOGLE_MAP_API_KEY")
