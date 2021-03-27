from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.donations, name='donations'),
    path('success', views.success, name='success'),
    path('checkout', views.checkout, name='checkout'),
]