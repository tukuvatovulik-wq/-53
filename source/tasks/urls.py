from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.task_list, name="list"),
    path("tasks/add/", views.task_create, name="create"),
    path("tasks/<int:pk>/", views.task_detail, name="detail"),
]
