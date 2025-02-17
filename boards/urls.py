from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('1', views.board_list),
]