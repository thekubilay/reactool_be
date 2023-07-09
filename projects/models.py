from django.db import models
from common.utils import generate_unique_id, generate_token_key
from companies.models import Company


def upload_to(instance, filename):
	return f"projects/{instance.id}/{filename}"


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
	STATUS = (
		("private", "非公開"),
		("public", "公開"),
		("archive", "アーカイブ"),
	)

	id = models.BigIntegerField(primary_key=True, blank=True)
	company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="projects")
	groups = models.ManyToManyField(ProjectGroup, blank=True, related_name="projects")
	logo = models.FileField(upload_to=upload_to, null=True, blank=True)
	name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=100, null=True, choices=STATUS,
														help_text="非公開, 公開, アーカイブ (非公開はトークン権限になる)", default="public")

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.id = generate_unique_id(self, 320)

		super().save(*args, **kwargs)


class ProjectToken(models.Model):
	id = models.BigIntegerField(primary_key=True, blank=True)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tokens")
	is_permanent = models.BooleanField(default=False)
	name = models.CharField(max_length=100, null=True, blank=True)
	key = models.CharField(max_length=100, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	expired_at = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.id = generate_unique_id(self, 330)

		if not self.key:
			self.key = generate_token_key()

		super().save(*args, **kwargs)
