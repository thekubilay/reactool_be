from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from projects.models import Project, ProjectGroup
from projects.serializers import ProjectSerializer, ProjectGroupSerializer


class ProjectRetrieveView(RetrieveAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer
	permission_classes = [AllowAny]


class ProjectGroupRetrieveView(RetrieveAPIView):
	queryset = ProjectGroup.objects.all()
	serializer_class = ProjectGroupSerializer
	permission_classes = [AllowAny]
