from django.urls import path
from . import views

urlpatterns = [
    path('second', views.s_page),
]