from django.urls import path, include
from .views import TaskViewSet, SubtaskViewSet, ContactViewSet, UserViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'subtasks', SubtaskViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
