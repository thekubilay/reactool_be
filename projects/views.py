from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from projects.models import Project, ProjectGroup
from projects.serializers import ProjectSerializer, ProjectWithGroupSerializer


class ProjectRetrieveView(RetrieveAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer
	permission_classes = [AllowAny]

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = self.get_serializer(instance)

		is_group = True if request.query_params.get("group", False) == "true" else False

		if is_group:
			serializer = ProjectWithGroupSerializer(instance)

		return Response(serializer.data)
