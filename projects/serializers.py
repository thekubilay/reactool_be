from projects.models import Project, ProjectGroup
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = "__all__"
		depth = 1


class ProjectGroupSerializer(serializers.ModelSerializer):
	projects = ProjectSerializer(many=True, read_only=True)

	class Meta:
		model = ProjectGroup
		fields = "__all__"
