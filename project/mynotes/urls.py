from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('tasks/', tasks, name='tasks'),
    path('add_task/', add_task, name='add_task'),
    path('tasks/delete/<int:pk>/', TaskDelete.as_view(), name='TaskDelete'),
    path('tasks/edit/<int:pk>/', TaskEdit.as_view(), name='TaskEdit'),
    path('toggle_task_complete/<int:pk>/', toggle_task_complete, name='toggle_task_complete'),
    path('untoggle_task_complete/<int:pk>/', untoggle_task_complete, name='untoggle_task_complete'),


]
