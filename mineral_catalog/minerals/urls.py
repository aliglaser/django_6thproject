from django.contrib import admin
from django.urls import path

from . import views


app_name = "minerals"

urlpatterns = [
	path('', views.mineral_list, name="mineral_list"),
    path('<int:pk>/', views.mineral_detail, name="mineral_detail"),
]
