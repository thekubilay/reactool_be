from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from projects.models import Project
from common.utils import generate_unique_id
from PIL import Image
from io import BytesIO


def upload_to(instance, filename):
	return f"plans/{instance.project.id}/{filename}"


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


class RoomPlan(models.Model):
	id = models.BigIntegerField(primary_key=True, blank=True)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="room_plans", null=True)
	order_num = models.IntegerField(null=True, default=1)
	is_list_hidden = models.BooleanField(default=False)
	is_archive = models.BooleanField(default=False)
	image = models.ImageField(upload_to=upload_to)
	thumbnail = models.ImageField(upload_to=upload_to, null=True, blank=True)
	type = models.CharField(max_length=255, blank=True, null=True, help_text="A, B, 立面図")
	ppm = models.FloatField(blank=True, null=True, help_text="1/100")
	menu = models.CharField(max_length=255, blank=True, null=True, help_text="基本...")
	madori = models.CharField(max_length=255, blank=True, null=True, help_text="2LDK, 4LDK+WIC")
	floor = models.CharField(max_length=255, blank=True, null=True, help_text="1F, 2F")
	measurement = models.CharField(max_length=255, blank=True, null=True, help_text="62.10m²")
	alcove = models.CharField(max_length=255, blank=True, null=True, help_text="2.50m²")
	terrace = models.CharField(max_length=255, blank=True, null=True, help_text="2.50m²")
	balcony = models.CharField(max_length=255, blank=True, null=True, help_text="2.50m²")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["order_num"]

	def __str__(self):
		return self.menu

	def save(self, *args, **kwargs):
		if not self.id:
			self.id = generate_unique_id(self, 510)

		self.size = self.image.size
		self.name = self.image.name

		if self.image:
			self.thumbnail = create_thumbnail(self.image)

		super().save(*args, **kwargs)


class GeneralPlan(models.Model):
	id = models.BigIntegerField(primary_key=True, blank=True)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="general_plans", null=True)
	order_num = models.IntegerField(null=True, default=1)
	image = models.ImageField(upload_to=upload_to)
	name = models.CharField(max_length=255, blank=True, null=True)
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

		if self.name == "":
			self.name = self.image.name

		super().save(*args, **kwargs)
