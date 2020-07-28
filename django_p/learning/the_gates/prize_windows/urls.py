from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='first_page'),
    path('contact',views.contact,name='contact'),
    path('login',views.login,name='login'),
    path('welcome',views.welcome,name='welcome'),
]