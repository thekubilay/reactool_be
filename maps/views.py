from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from maps.models import Map, MapCategory, Project
from maps.serializers import MapSerializer, MapCategorySerializer


class MapListAPIView(ListAPIView):
	serializer_class = MapSerializer
	permission_classes = [AllowAny]

	def get_queryset(self):
		project_id = self.kwargs.get("project_id")
		projects = Project.objects.filter(id=project_id)
		project = projects.first()

		if not project:
			return Map.objects.none()

		queryset = Map.objects.filter(project=project)

		if project.status == "archive":
			return None

		if project.status == "public":
			return queryset

		token = project.tokens.filter(key=self.request.query_params.get("token", None)).first()

		if not token:
			return Map.objects.none()

		if token.is_permanent or (token.expired_at and token.expired_at > timezone.now()):
			return queryset

		return None

	def list(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		serializer = self.get_serializer(queryset, many=True)

		if queryset is not None:
			return Response(serializer.data, status=status.HTTP_200_OK)

		return Response({"message": "Access token is invalid."}, status=status.HTTP_403_FORBIDDEN)


class MapCategoryListAPIView(ListAPIView):
	queryset = MapCategory.objects.all()
	serializer_class = MapCategorySerializer
	permission_classes = [AllowAny]

	def get_queryset(self):
		project_id = self.kwargs.get("project_id")
		projects = Project.objects.filter(id=project_id)
		project = projects.first()

		if not project:
			return MapCategory.objects.none()

		queryset = MapCategory.objects.filter(project=project)

		if project.status == "archive":
			return None

		if project.status == "public":
			return queryset

		token = project.tokens.filter(key=self.request.query_params.get("token", None)).first()

		if not token:
			return MapCategory.objects.none()

		if token.is_permanent or (token.expired_at and token.expired_at > timezone.now()):
			return queryset

		return None

	def list(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		serializer = self.get_serializer(queryset, many=True)

		if queryset is not None:
			return Response(serializer.data, status=status.HTTP_200_OK)

		return Response({"message": "Access token is invalid."}, status=status.HTTP_403_FORBIDDEN)
