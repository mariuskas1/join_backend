from .serializers import TaskSerializer, SubtaskSerializer, ContactSerializer, UserSerializer
from join_app.models import Task, Subtask, Contact, User
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


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