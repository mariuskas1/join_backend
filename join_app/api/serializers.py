from rest_framework import serializers
from join_app.models import Task, Subtask, Contact, User


class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True, required=False)  # Use the correct related_name

    class Meta:
        model = Task
        fields = '__all__'

    def update(self, instance, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        current_subtasks = {subtask.id: subtask for subtask in instance.subtasks.all()} 
        new_subtasks = []

        for subtask_data in subtasks_data:
            subtask_id = subtask_data.get('id')
            if subtask_id in current_subtasks:
                subtask_instance = current_subtasks.pop(subtask_id)
                for attr, value in subtask_data.items():
                    setattr(subtask_instance, attr, value)
                subtask_instance.save()
            else:
                new_subtasks.append(Subtask(task=instance, **subtask_data))

        for subtask in current_subtasks.values():
            subtask.delete()

        if new_subtasks:
            Subtask.objects.bulk_create(new_subtasks)

        return instance



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'