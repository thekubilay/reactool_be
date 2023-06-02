from rest_framework import serializers
from routes.models import Route


class RouteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Route
		fields = "__all__"
		depth = 1
