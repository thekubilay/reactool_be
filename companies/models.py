from django.db import models
from users.models import User
from common.utils import generate_unique_id


class Company(models.Model):
	id = models.BigIntegerField(primary_key=True, blank=True)
	name = models.CharField(max_length=100)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="companies")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.id = generate_unique_id(self, 300)

		super().save(*args, **kwargs)
