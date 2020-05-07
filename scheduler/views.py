from scheduler.models import Schedule
from rest_framework import viewsets
from rest_framework import permissions
from scheduler.serializers import ScheduleSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
  queryset = Schedule.objects.all()
  serializer_class = ScheduleSerializer
