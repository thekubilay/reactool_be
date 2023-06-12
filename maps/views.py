from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from maps.models import Map, MapCategory
from maps.serializers import MapSerializer, MapCategorySerializer


class MapListAPIView(ListAPIView):
	queryset = Map.objects.all()
	serializer_class = MapSerializer
	permission_classes = [AllowAny]

	def get_queryset(self):
		project_id = self.kwargs['project_id']
		return Map.objects.filter(project_id=project_id)


class MapCategoryListAPIView(ListAPIView):
	queryset = MapCategory.objects.all()
	serializer_class = MapCategorySerializer
	permission_classes = [AllowAny]

	def get_queryset(self):
		project_id = self.kwargs['project_id']
		return MapCategory.objects.filter(project_id=project_id)
