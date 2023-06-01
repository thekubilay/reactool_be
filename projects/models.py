from django.db import models
from common.utils import generate_unique_id
from companies.models import Company


class ProjectGroup(models.Model):
	id = models.BigIntegerField(primary_key=True, blank=True)
	name = models.CharField(max_length=100)
	company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="groups")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.id = generate_unique_id(self, 310)

		super().save(*args, **kwargs)


class Project(models.Model):
	id = models.BigIntegerField(primary_key=True, blank=True)
	company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="projects")
	groups = models.ManyToManyField(ProjectGroup, blank=True, related_name="projects")
	name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.id = generate_unique_id(self, 320)

		super().save(*args, **kwargs)
