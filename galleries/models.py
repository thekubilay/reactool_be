from django.db import models
from common.utils import generate_unique_id
from projects.models import Project


def upload_to(instance, filename):
	return f"galleries/{instance.project.id}/{filename}"


class Gallery(models.Model):
	id = models.BigIntegerField(primary_key=True, blank=True)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="galleries")
	url = models.FileField(upload_to=upload_to)
	name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.id = generate_unique_id(self, 410)

		super().save(*args, **kwargs)
