from django.db import models
from projects.models import Project
from common.utils import generate_unique_id


class Route(models.Model):
	id = models.BigIntegerField(primary_key=True, blank=True)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="routes")
	order_num = models.IntegerField(null=True, default=1)
	route_name = models.CharField(max_length=255, blank=True)
	component_name = models.CharField(max_length=255, blank=True)
	endpoint = models.CharField(max_length=255, blank=True)
	front_url_name = models.CharField(max_length=255, blank=True)

	class Meta:
		ordering = ["order_num"]

	def __str__(self):
		return self.component_name

	def save(self, *args, **kwargs):
		if not self.id:
			self.id = generate_unique_id(self, 610)

		super().save(*args, **kwargs)
