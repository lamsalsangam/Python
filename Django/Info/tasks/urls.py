from django.urls import path

from . import views

# app_name is desginated to prevent the happening of the name space collision
app_name = "tasks"
urlpatterns = [
    path("", views.index,name="index"),
    path("add",views.add,name="add")
]