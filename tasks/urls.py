from django.urls import path
from .views import TaskListCreateAPIView, TaskUpdateAPIView

urlpatterns = [
    path("", TaskListCreateAPIView.as_view(), name="task-list-create"),
    path("<int:pk>/", TaskUpdateAPIView.as_view(), name="task-update"),
]
