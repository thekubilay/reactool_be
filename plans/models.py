from django.db import models
from projects.models import Project
from common.utils import generate_unique_id


def upload_to(instance, filename):
	return f"plans/{instance.project.id}/{filename}"


class Plan(models.Model):
	KIND = (
		("general_plan", "一般図"),
		("room_plan", "間取り図"),
	)

	id = models.BigIntegerField(primary_key=True, blank=True)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="plans", null=True)
	order_num = models.IntegerField(null=True, default=1)
	plan = models.CharField(max_length=255, blank=True, choices=KIND, default="general_plan",
													help_text="一般図 間取り図", )
	image = models.FileField(upload_to=upload_to)
	type = models.CharField(max_length=255, blank=True, null=True, help_text="A, B")
	menu = models.CharField(max_length=255, blank=True, null=True, help_text="基本...")
	madori = models.CharField(max_length=255, blank=True, null=True, help_text="2LDK, 4LDK+WIC")
	measurement = models.CharField(max_length=255, blank=True, null=True, help_text="6.0m×6.0m")
	alcove = models.CharField(max_length=255, blank=True, null=True, help_text="2.50m²")
	terrace = models.CharField(max_length=255, blank=True, null=True, help_text="2.50m²")
	balcony = models.CharField(max_length=255, blank=True, null=True, help_text="2.50m²")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["order_num"]

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.id = generate_unique_id(self, 510)

		self.size = self.image.size
		self.name = self.image.name

		super().save(*args, **kwargs)
