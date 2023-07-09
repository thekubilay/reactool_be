from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from documents.models import Document
from documents.serializers import DocumentSerializer


class DocumentListAPIView(ListAPIView):
	queryset = Document.objects.all()
	serializer_class = DocumentSerializer
	permission_classes = [AllowAny]

	def get_queryset(self):
		project_id = self.kwargs['project_id']
		return Document.objects.filter(project_id=project_id)
