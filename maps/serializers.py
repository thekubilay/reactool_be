from maps.models import Map, MapCategory, MapImage
from rest_framework import serializers


class MapImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = MapImage
		fields = '__all__'


class MapSerializer(serializers.ModelSerializer):
	images = MapImageSerializer(many=True, read_only=True)

	class Meta:
		model = Map
		fields = '__all__'


class MapCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = MapCategory
		fields = '__all__'
