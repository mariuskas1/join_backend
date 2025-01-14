from .serializers import TaskSerializer, SubtaskSerializer, ContactSerializer, UserSerializer
from join_app.models import Task, Subtask, Contact, User
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response




class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        task_data = request.data
        subtasks_data = task_data.pop('subtasks', [])

        # Create the task object first
        task = Task.objects.create(**task_data)

        # Create subtasks if any
        for subtask_data in subtasks_data:
            Subtask.objects.create(task=task, **subtask_data)

        # Now return the task with subtasks
        task_serializer = TaskSerializer(task)
        return Response(task_serializer.data)


class SubtaskViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer


class ContactViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer