from django.db import models
from projects.models import Project
from common.utils import generate_unique_id


def upload_to(instance, filename):
	return f"panorama/{instance.project.id}/{filename}"


class Panorama(models.Model):
	DAY_TIMES = (
		("morning", "朝"),
		("afternoon", "昼"),
		("evening", "夕"),
		("night", "夜"),
	)

	id = models.BigIntegerField(primary_key=True, blank=True)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="panorama", null=True)
	name = models.CharField(max_length=100)
	type = models.CharField(max_length=100, null=True, blank=True, help_text="A, B, (子文字入力してもでアッパーケースに交換)")
	day_time = models.CharField(max_length=100, null=True, blank=True, choices=DAY_TIMES, help_text="朝, 昼, 夕, 夜")
	image = models.FileField(upload_to=upload_to, null=True, blank=True)
	is_loop = models.BooleanField(default=True, help_text="ループするかどうか")
	is_panoramic = models.BooleanField(default=True, help_text="パノラマ写真かどうか")
	floor = models.IntegerField(null=True, default=1, help_text="何階か")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.id = generate_unique_id(self, 710)

		super().save(*args, **kwargs)
