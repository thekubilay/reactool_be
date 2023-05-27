from django.test import TestCase
from users.models import User


def create_superuser(email, password):
	return User.objects.create_superuser(email, password)


create_superuser("kubilay.turgut@gmail.com", "324131")
