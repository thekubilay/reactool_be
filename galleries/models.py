from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from common.utils import generate_unique_id
from projects.models import Project


def upload_to(instance, filename):
	return f"galleries/{instance.project.id}/{filename}"


def create_thumbnail(image):
	# Open the image using Pillow
	img = Image.open(image)

	# Convert RGBA image to RGB
	if img.mode == 'RGBA':
		img = img.convert('RGB')

	# Resize the image to a smaller size for the thumbnail
	thumbnail_size = (300, 300)
	img.thumbnail(thumbnail_size)

	# Create a BytesIO object to temporarily hold the thumbnail
	thumb_io = BytesIO()

	# Save the thumbnail image to the BytesIO object
	img.save(thumb_io, format='JPEG', quality=50)

	# Create a new InMemoryUploadedFile for the thumbnail image
	thumbnail = InMemoryUploadedFile(
		thumb_io,
		None,
		f"{image.name.split('.')[0]}_thumbnail.jpg",
		'image/jpeg',
		thumb_io.tell(),
		None
	)

	return thumbnail


class Gallery(models.Model):
	id = models.BigIntegerField(primary_key=True, blank=True)
	order_num = models.IntegerField(null=True, default=1)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="galleries")
	file = models.FileField(upload_to=upload_to)
	thumbnail = models.ImageField(upload_to=upload_to, null=True, blank=True)
	name = models.CharField(max_length=255, blank=True)
	size = models.IntegerField(null=True, default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = "Galleries"
		ordering = ["order_num"]

	def __str__(self):
		return self.project.name + "'s - " + self.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.id = generate_unique_id(self, 410)

		self.size = self.file.size
		self.name = self.file.name

		if self.file:
			self.thumbnail = create_thumbnail(self.file)

		super().save(*args, **kwargs)
