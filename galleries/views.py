from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from galleries.models import Gallery
from galleries.serializers import GallerySerializer


class GalleryRetrieveAPIView(RetrieveAPIView):
	queryset = Gallery.objects.all()
	serializer_class = GallerySerializer
	lookup_field = 'pk'
	permission_classes = [AllowAny]
