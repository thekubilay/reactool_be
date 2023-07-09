from django.db import models


class Room(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	capacity = models.IntegerField()
	projector = models.BooleanField(default=False)

	def __str__(self):
		return self.name
