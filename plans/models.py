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
	plan_type = models.CharField(max_length=255, blank=True, choices=KIND, default="general_plan")
	name = models.CharField(max_length=255, blank=True, help_text="A, B or 敷地配置図")
	image = models.FileField(upload_to=upload_to)
	room_type = models.CharField(max_length=255, blank=True, null=True, help_text="2LDK, 4LDK+WIC")
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
