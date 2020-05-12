from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('profile/', views.profile, name = "profile"),
    path('future/', views.future, name = "future"),
    path('future/create', views.create, name = "create"),
]