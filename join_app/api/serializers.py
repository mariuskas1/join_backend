from rest_framework import serializers
from join_app.models import Task, Subtask


class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True)
    
    class Meta:
        model = Task
        fields = '__all__'