from django.urls import path
from plans.views import PlanListAPIView

urlpatterns = [
	path('<int:project_id>/plans/', PlanListAPIView.as_view(), name='plan_list'),
]
