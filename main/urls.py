from django.urls import path
from . import views

urlpattern = [
    path('<str:key>/', views.home, name='home')
]