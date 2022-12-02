from django.contrib import admin
from django.urls import path
from todoList import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path("search", views.search, name="search"),
    path('delete/<str:task_name>', views.delete, name='delete'),
    path('update/<str:task_name>', views.update, name='Update'),
]
