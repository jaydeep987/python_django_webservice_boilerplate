""" URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from django.conf import settings

urlpatterns = [
	path('scheduler/', include('scheduler.urls')),

	# This generates open api schema dynamically, and it is referenced at swagger-ui/ path
	# This we can allow only in STG and DEV if API is not open, but for now, no limit!
	path('openapi', get_schema_view(
		title='python-django-web-service',
		description='A boilerplate for getting started with python web service',
		version='1.0.0'
	), name='openapi-schema'),
	path('swagger-ui/', TemplateView.as_view(
		template_name='swagger-ui.html',
		extra_context={'schema_url': 'openapi-schema'}
	), name='swagger-ui'),
]

if settings.ADMIN_ENABLED is True:
	urlpatterns += [
		path('admin/', admin.site.urls),
	]
