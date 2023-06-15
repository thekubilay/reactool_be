from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from plans.models import RoomPlan, GeneralPlan
from plans.serializers import GeneralPlanSerializer, RoomPlanSerializer


class RoomPlanListAPIView(ListAPIView):
	queryset = RoomPlan.objects.all()
	serializer_class = RoomPlanSerializer
	permission_classes = [AllowAny]

	def get_queryset(self):
		project_id = self.kwargs['project_id']
		return RoomPlan.objects.filter(project_id=project_id)


class GeneralPlanListAPIView(ListAPIView):
	queryset = GeneralPlan.objects.all()
	serializer_class = GeneralPlanSerializer
	permission_classes = [AllowAny]

	def get_queryset(self):
		project_id = self.kwargs['project_id']
		return GeneralPlan.objects.filter(project_id=project_id)
