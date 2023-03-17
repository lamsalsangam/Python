from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("geek", views.geek, name="geek"),
    path("<str:name>", views.greet, name="greet"),
]