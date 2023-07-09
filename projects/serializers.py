from rest_framework import serializers
from projects.models import Project, ProjectGroup
from routes.serializers import RouteSerializer
from galleries.serializers import GallerySerializer


class ProjectSerializer(serializers.ModelSerializer):
	routes = RouteSerializer(many=True, read_only=True)
	galleries = GallerySerializer(many=True, read_only=True)

	class Meta:
		model = Project
		exclude = ["company", "groups"]
		depth = 1


class ProjectWithGroupSerializer(serializers.ModelSerializer):
	routes = RouteSerializer(many=True, read_only=True)
	galleries = GallerySerializer(many=True, read_only=True)

	class Meta:
		model = Project
		exclude = ["company"]
		depth = 1


class ProjectGroupSerializer(serializers.ModelSerializer):
	projects = ProjectSerializer(many=True, read_only=True)

	class Meta:
		model = ProjectGroup
		fields = "__all__"
