from django.contrib import admin
from .models import Contact, Task, Subtask

admin.site.register(Contact)
admin.site.register(Task)
admin.site.register(Subtask)