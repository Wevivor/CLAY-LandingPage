from django.contrib import admin
from django.urls import path
from .views import share, notice

urlpatterns = [
    path('shared/', share, name='share'),
    path('notice/',notice,name='notice'),
]