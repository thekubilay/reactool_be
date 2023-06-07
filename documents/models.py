import boto3
import tempfile
import os

from decouple import config

from django.core.files.base import ContentFile
from django.db import models
from projects.models import Project
from common.utils import generate_unique_id
from django.utils.html import mark_safe
from pdf2image import convert_from_path


def upload_to(instance, filename):
	return f"documents/{instance.project.id}/{filename}"


class Document(models.Model):
	id = models.BigIntegerField(primary_key=True, blank=True)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="documents", null=True)
	order_num = models.IntegerField(null=True, default=1)
	name = models.CharField(max_length=255, blank=True, null=True)
	thumbnail = models.ImageField(upload_to=upload_to, blank=True)
	file = models.FileField(upload_to='documents/%Y/%m/%d')
	size = models.IntegerField(null=True, default=1)
	type = models.CharField(max_length=255, blank=True, null=True)
	uploaded_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["order_num"]

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.id = generate_unique_id(self, 810)

		self.name = self.file.name
		self.size = self.file.size
		self.type = self.file.file.content_type
