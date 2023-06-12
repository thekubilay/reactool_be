from django.db import models
from projects.models import Project
from common.utils import generate_unique_id


def upload_to(instance, filename):
	return f"maps/{instance.map.project.id}/{filename}"


class Map(models.Model):
	id = models.BigIntegerField(primary_key=True, blank=True)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="maps", null=True)
	order_num = models.IntegerField(null=True, default=1)
	category = models.ForeignKey("MapCategory", on_delete=models.CASCADE, related_name="maps", null=True)
	name = models.CharField(max_length=255, blank=True, null=True, help_text="AEON MALL")
	address = models.CharField(max_length=255, blank=True, null=True, help_text="〒000-0000 東京都渋谷区渋谷1-1-1")
	lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
	lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["order_num"]

	def __str__(self):
		return self.name

	def category_name(self):
		return self.category.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.id = generate_unique_id(self, 610)

		super().save(*args, **kwargs)


class MapImage(models.Model):
	id = models.BigIntegerField(primary_key=True, blank=True)
	map = models.ForeignKey(Map, on_delete=models.CASCADE, related_name="images", null=True)
	order_num = models.IntegerField(null=True, default=1)
	image = models.FileField(upload_to=upload_to, null=True, blank=True)

	class Meta:
		ordering = ["order_num"]

	def __str__(self):
		return self.image.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.id = generate_unique_id(self, 620)

		super().save(*args, **kwargs)


class MapCategory(models.Model):
	id = models.BigIntegerField(primary_key=True, blank=True)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="map_categories", null=True)
	order_num = models.IntegerField(null=True, default=1)
	name = models.CharField(max_length=255, blank=True, null=True)

	class Meta:
		ordering = ["order_num"]

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.id = generate_unique_id(self, 630)

		super().save(*args, **kwargs)
