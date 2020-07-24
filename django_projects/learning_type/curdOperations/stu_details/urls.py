from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('add/', views.add_show, name = "addandshow"),
    path('<int:id>/', views.update_show, name = "updateshow"),
    path('delete/<int:id>/', views.delete_data, name = "deletedata"),
]