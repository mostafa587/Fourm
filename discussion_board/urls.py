"""
URL configuration for discussion_board project.

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
from django.urls import path ,include 
from django.contrib import admin
from rest_framework import routers # Routers help you automatically generate URL patterns for your API endpoints. Instead of writing a ton of URL rules manually, DRF's router does it for you.
# router also is a way to directing traffic to the API (view functions)
router = routers.DefaultRouter() # DefaultRouter is like your personal URL manager. When you register your API viewsets with it, it automatically sets up all the standard routes (like list, retrieve, create, update, delete).

urlpatterns = router.urls

urlpatterns += [ # += is used to add URLs not to overwrite on urlpatterns
    path('admin/', admin.site.urls),
    path('', include('boards.urls')),
]
