from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from panorama.models import Panorama
from panorama.serializers import PanoramaSerializer


class PanoramaListAPIView(ListAPIView):
	queryset = Panorama.objects.all()
	serializer_class = PanoramaSerializer
	permission_classes = [AllowAny]

	def get_queryset(self):
		project_id = self.kwargs['project_id']
		return Panorama.objects.filter(project_id=project_id)
