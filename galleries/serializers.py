from rest_framework import serializers
from galleries.models import Gallery


class GallerySerializer(serializers.ModelSerializer):
	class Meta:
		model = Gallery
		fields = "__all__"
		read_only_fields = ['id', 'created_at', 'updated_at']
