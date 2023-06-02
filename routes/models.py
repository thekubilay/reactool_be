from django.db import models
from projects.models import Project
from common.utils import generate_unique_id


class Route(models.Model):
	id = models.BigIntegerField(primary_key=True, blank=True)
	order_num = models.IntegerField(null=True, default=1)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="routes")
	route_name = models.CharField(max_length=255, blank=True)
	component_name = models.CharField(max_length=255, blank=True)
	url_name = models.CharField(max_length=255, blank=True)

	def endpoint(self):
		return f"{self.project.id}/{self.url_name}/"

	class Meta:
		ordering = ["order_num"]

	def __str__(self):
		return self.component_name

	def save(self, *args, **kwargs):
		if not self.id:
			self.id = generate_unique_id(self, 610)

		super().save(*args, **kwargs)
