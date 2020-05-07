from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'schedule', views.ScheduleViewSet)

urlpatterns = [
    path('', include(router.urls))
]
