import random

from django.db.models import Model


def generate_unique_id(instance: Model, prefix: int):
	pk = random.randint(1000000000, 9999999999)
	pk = str(prefix) + str(pk)
	while instance.objects.filter(pk=pk).exists():
		pk = random.randint(1000000000, 9999999999)
		pk = str(prefix) + str(pk)

	return pk
