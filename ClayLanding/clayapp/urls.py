from django.contrib import admin
from django.urls import path
from .views import index, complete

urlpatterns = [
    path('', index, name='index'),
    path('complete/', complete, name='complete'),
]
