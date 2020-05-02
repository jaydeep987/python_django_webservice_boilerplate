from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'djangodemo', views.DjangoDemoViewSet)

urlpatterns = [
    path('', include(router.urls))
]
