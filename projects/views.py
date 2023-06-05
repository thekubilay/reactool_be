from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.utils import timezone
from projects.models import Project, ProjectToken, ProjectGroup
from projects.serializers import ProjectSerializer, ProjectWithGroupSerializer


class ProjectRetrieveView(RetrieveAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer
	permission_classes = [AllowAny]

	def retrieve(self, request, *args, **kwargs):
		instance: Project = self.get_object()
		serializer = self.get_serializer(instance)

		is_group = True if request.query_params.get("group", False) == "true" else False
		key = request.query_params.get("token", None)

		if instance.status == "private":
			token: ProjectToken = instance.tokens.filter(key=key).first()

			if token is None:
				return Response({"detail": "Project access token is invalid."}, status=403)

			if token.is_permanent:
				if is_group:
					serializer = ProjectWithGroupSerializer(instance)

				return Response(serializer.data)
			else:
				if token.expired_at is not None and token.expired_at > timezone.now():
					if is_group:
						serializer = ProjectWithGroupSerializer(instance)

					return Response(serializer.data)
				else:
					return Response({"detail": "Project access token has expired."}, status=403)
