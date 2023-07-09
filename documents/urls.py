from django.urls import path
from documents.views import DocumentListAPIView

urlpatterns = [
	path('<int:project_id>/documents/', DocumentListAPIView.as_view(), name='document_list'),
]
