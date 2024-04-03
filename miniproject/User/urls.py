from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_user),
    path('<int:id>/', views.get_user),
    path('delete/<int:id>/', views.delete_user)
]