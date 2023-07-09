from panorama.models import Panorama
from rest_framework import serializers


class PanoramaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Panorama
		fields = '__all__'
