"""
URL configuration for edirbackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include,re_path
from djoser import views as djoser_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
#    path('api/rest-auth/',include('rest_auth.urls')),
    # path('api/rest-auth/registration/', include('rest_auth.registration.urls')),
    # path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('django-rest-allauth/', include('django_rest_allauth.api.urls')),
    # path('accounts/', include('allauth.urls')),
    # path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # re_path(r'^rest-auth/', include(rest_auth_urls)),
    path('auth/',include('djoser.urls')),
     path('auth/',include('djoser.urls.jwt')),
     path('test/',include('core.urls')),
]
