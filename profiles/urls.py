from django.contrib import admin
from django.urls import path, include

from . import views


app_name = "profiles"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:username>/", views.profile, name="profile"),
]
