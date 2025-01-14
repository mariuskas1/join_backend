from django.urls import path, include
from .views import TaskViewSet, SubtaskViewSet, ContactViewSet, UserViewSet
from rest_framework import routers
from rest_framework_nested import routers


router = routers.SimpleRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'subtasks', SubtaskViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'users', UserViewSet)

tasks_router = routers.NestedSimpleRouter(router, r'tasks', lookup='task')
tasks_router.register(r'subtasks', SubtaskViewSet, basename='task-subtask')


urlpatterns = [
    path('', include(router.urls)),
]
