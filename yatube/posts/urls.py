from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('groups/<slug:slug>', views.group_posts),
]
