from rest_framework import serializers
from projects.models import Project, ProjectGroup
from routes.serializers import RouteSerializer


class ProjectSerializer(serializers.ModelSerializer):
	routes = RouteSerializer(many=True, read_only=True)

	class Meta:
		model = Project
		fields = "__all__"
		depth = 1


class ProjectGroupSerializer(serializers.ModelSerializer):
	projects = ProjectSerializer(many=True, read_only=True)

	class Meta:
		model = ProjectGroup
		fields = "__all__"
