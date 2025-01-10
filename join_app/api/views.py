from .serializers import TaskSerializer, SubtaskSerializer
from join_app.models import Task, Subtask
from rest_framework import generics, viewsets


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class SubtasktViewSet(viewsets.ModelViewSet):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer