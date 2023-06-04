from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from plans.models import Plan
from plans.serializers import PlanSerializer


class PlanListAPIView(ListAPIView):
	queryset = Plan.objects.all()
	serializer_class = PlanSerializer
	permission_classes = [AllowAny]

	def get_queryset(self):
		project_id = self.kwargs['project_id']
		return Plan.objects.filter(project_id=project_id)

