from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('tutorials/', views.taskList, name="task-list"),
    path('tutorials/<str:pk>/', views.taskDetail, name="task-Detail"),
    path('tutorials/<str:pk>/', views.taskUpdate, name="task-update"),
    path('tutorials/', views.taskCreate, name="task-Create"),
    path('tutorials/<str:pk>/', views.taskDelete, name="task-delete"),
]