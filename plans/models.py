from django.db import models
from common.utils import generate_unique_id


def upload_to(instance, filename):
	return f"plans/{instance.project.id}/{filename}"


class BuildingPlan(models.Model):
	id = models.BigIntegerField(primary_key=True, blank=True)
	order_num = models.IntegerField(null=True, default=1)
	name = models.CharField(max_length=255, blank=True)
	image = models.FileField(upload_to=upload_to)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["order_num"]

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.id = generate_unique_id(self, 510)

		self.size = self.url.size
		self.name = self.url.name

		super().save(*args, **kwargs)
