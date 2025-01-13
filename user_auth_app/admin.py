from django.contrib import admin

from user_auth_app.models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')  # Fields to show in the list view
    search_fields = ('name', 'user__email')  # Enable searching by name and email