from django.urls import path

from .views import myintro

urlpatterns = [
    path("", myintro, name="myintro")
]
