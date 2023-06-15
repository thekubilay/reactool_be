from django.utils import timezone
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from projects.models import Project, ProjectToken, ProjectGroup
from projects.serializers import ProjectSerializer, ProjectWithGroupSerializer


class ProjectRetrieveView(RetrieveAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer
	# permission_classes = [AllowAny]

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = self.get_serializer(instance)

		is_group = request.query_params.get("group", False) == "true"
		key = request.query_params.get("token")

		if instance.status == "private":
			token = instance.tokens.filter(key=key).first()

			if not token:
				return Response({"detail": "Project access token is invalid."}, status=status.HTTP_403_FORBIDDEN)

			if token.is_permanent or (token.expired_at and token.expired_at > timezone.now()):
				if is_group:
					serializer = ProjectWithGroupSerializer(instance)

				return Response(serializer.data)

			return Response({"detail": "Project access token has expired."}, status=status.HTTP_403_FORBIDDEN)

		return Response(serializer.data, status=status.HTTP_200_OK)
