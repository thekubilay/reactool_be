from rest_framework import serializers
from galleries.models import Gallery


class GallerySerializer(serializers.ModelSerializer):
	class Meta:
		model = Gallery
		fields = "__all__"
