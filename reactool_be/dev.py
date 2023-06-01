from decouple import config

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

AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = "development-r-bucket"
AWS_S3_REGION_NAME = 'ap-northeast-3'

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_FILE_OVERWRITE = True

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com/media/'

STATICFILES_STORAGE = 'reactool_be.storages.StaticS3Boto3Storage'
DEFAULT_FILE_STORAGE = 'reactool_be.storages.MediaS3Boto3Storage'

EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
