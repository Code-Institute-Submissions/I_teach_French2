from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.donations, name='donations'),
    path('charge/', views.charge, name='charge'),
    path('success/<str:args>/', views.successMsg, name="success"),
]