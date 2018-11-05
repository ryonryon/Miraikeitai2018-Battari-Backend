from django.urls import path

from . import views

urlpatterns = [
    path('firebase', views.firebase, name='firebase'),
]