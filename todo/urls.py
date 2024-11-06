from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
    path('tasks/', views.task_list, name='task_list'), 
    path('task/create/', views.task_create, name='task_create'),
    path('task/<int:task_id>/edit/', views.task_edit, name='task_edit'),
    path('task/<int:task_id>/delete/', views.task_delete, name='task_delete'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
