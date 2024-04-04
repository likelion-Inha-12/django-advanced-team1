from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_user),
    path('<int:id>/', views.get_user),
    path('delete/<int:id>/', views.delete_user),
    path('appoint/<int:id>/', views.appoint_user),
    path('listall/', views.list_all)
]