from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from galleries.models import Gallery
from galleries.serializers import GallerySerializer


class GalleryListAPIView(ListAPIView):
	queryset = Gallery.objects.all()
	serializer_class = GallerySerializer
	permission_classes = [AllowAny]

	def get_queryset(self):
		project_id = self.kwargs['project_id']
		return Gallery.objects.filter(project_id=project_id)
