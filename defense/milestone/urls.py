import allauth
from django.urls import path
from milestone import forms, views
from allauth.account import views
from milestone import views
urlpatterns = [
    path('', views.home, name='home'),

]