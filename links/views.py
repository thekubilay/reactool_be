from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from links.models import Link
from links.serializers import LinkSerializer


class LinkListAPIView(ListAPIView):
	queryset = Link.objects.all()
	serializer_class = LinkSerializer
	permission_classes = [AllowAny]

	def get_queryset(self):
		project_id = self.kwargs['project_id']
		return Link.objects.filter(project_id=project_id)

