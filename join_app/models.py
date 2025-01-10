from django.db import models

# Create your models here.

#tasks, subtask, users, contacts


PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('await_feedback', 'Await Feedback'),
        ('done', 'Done'),
    ]


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    date = models.DateField()
    prio = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    assignedTo = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    id = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.title
    
    
class Subtask(models.Model):
    title = models.CharField(max_length=255)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')

    def __str__(self):
        return self.title