from django.test import TestCase
from users.models import User


def create_superuser(email, password):
	return User.objects.create_superuser(email, password)


create_superuser("morisaki@nulunus.com", "324131")
