from django.contrib import admin
from django.urls import path
from .views import TaskViewSet

urlpatterns = [
    path('', TaskViewSet.as_view()),
]
