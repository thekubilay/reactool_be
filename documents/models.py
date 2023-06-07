from django.core.files.base import ContentFile
from django.db import models
from projects.models import Project
from common.utils import generate_unique_id
from django.utils.html import mark_safe
from pdf2image import convert_from_path



def upload_to(instance, filename):
	return f"documents/{instance.project.id}/{filename}"


def generate_pdf_thumbnail(pdf_file):
	pages = convert_from_path(pdf_file.path, dpi=200)  # Convert the PDF file to images
	if pages:
		first_page = pages[0]
		thumbnail_content = ContentFile()
		first_page.save(thumbnail_content, 'JPEG')
		return thumbnail_content


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

	def thumbnail_tag(self):
		return mark_safe('<img src="%s" width="150" height="150" />' % (self.thumbnail.url if self.thumbnail else ''))

	thumbnail_tag.short_description = 'Thumbnail'

	def save(self, *args, **kwargs):
		if not self.id:
			self.id = generate_unique_id(self, 810)

		self.name = self.file.name
		self.size = self.file.size
		self.type = self.file.file.content_type

		if not self.id and self.file:
			thumbnail_content = generate_pdf_thumbnail(self.file)
			self.thumbnail.save(f"{self.file.name}.thumbnail.jpg", thumbnail_content, save=False)

			# Upload the thumbnail to AWS S3 bucket
			s3_client = boto3.client('s3')
			s3_key = f"documents/{self.project.id}/{self.file.name}.thumbnail.jpg"
			s3_client.upload_fileobj(thumbnail_content, 'your-s3-bucket-name', s3_key)

		super().save(*args, **kwargs)
