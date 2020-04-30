from polls.models import DjangoDemo
from rest_framework import viewsets
from rest_framework import permissions
from polls.serializers import DjangoDemoSerializer

class DjangoDemoViewSet(viewsets.ModelViewSet):
  queryset = DjangoDemo.objects.all()
  serializer_class = DjangoDemoSerializer
