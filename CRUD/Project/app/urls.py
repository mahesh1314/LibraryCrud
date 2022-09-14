from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('insert', views.insertData, name="insertData"),
    path('update/<id>',views.updateData, name="updateData"),
    path('delete/<id>',views.delete, name="delete"),
    path('about',views.about, name="about"),
    path('', views.home, name="home"),

   
]
