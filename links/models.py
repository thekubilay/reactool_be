from django.db import models
from projects.models import Project
from common.utils import generate_unique_id


def upload_to(instance, filename):
	return f"links/{instance.project.id}/{filename}"


class Link(models.Model):
	id = models.BigIntegerField(primary_key=True, blank=True)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="links", null=True)
	name = models.CharField(max_length=255, blank=True, null=True)
	url = models.CharField(max_length=255, blank=True, null=True)
	image = models.ImageField(upload_to=upload_to, blank=True, null=True)
	order_num = models.IntegerField(null=True, default=1)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["order_num"]

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.id = generate_unique_id(self, 710)

		super().save(*args, **kwargs)
