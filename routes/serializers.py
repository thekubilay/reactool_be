from rest_framework import serializers
from routes.models import Route


class RouteSerializer(serializers.ModelSerializer):
	endpoint = serializers.CharField(read_only=True)

	class Meta:
		model = Route
		fields = "__all__"
		depth = 1
