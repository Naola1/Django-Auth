from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for UserProfile model
    - Displays user, location, and birth date in list view
    - Enables search by username, email, and location
    """
    list_display = ('user', 'location', 'birth_date')
    search_fields = ('user__username', 'user__email', 'location')
