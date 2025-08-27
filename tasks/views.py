from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .models import Task
from .serializers import TaskSerializer


class TaskListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.filter(user=request.user).order_by("-created_at")
        serializer = TaskSerializer(tasks, many=True)
        return Response(
            {"success": True, "tasks": serializer.data},
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                {"success": True, "message": "Task created successfully", "task": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"success": False, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class TaskUpdateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        serializer = TaskSerializer(task)
        return Response(
            {"success": True, "task": serializer.data},
            status=status.HTTP_200_OK,
        )

    def put(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        serializer = TaskSerializer(task, data=request.data, partial=True)  # allow partial update
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                {"success": True, "message": "Task updated successfully", "task": serializer.data},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"success": False, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.delete()
        return Response(
            {"success": True, "message": "Task deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )
