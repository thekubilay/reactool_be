import random

from django.db.models import Model


def generate_unique_id(instance: Model, prefix: int):
	pk = random.randint(1000000, 9999999)
	pk = str(prefix) + str(pk)

	while instance.__class__.objects.filter(pk=pk).exists():
		pk = random.randint(1000000, 9999999)
		pk = str(prefix) + str(pk)

	return int(pk)
