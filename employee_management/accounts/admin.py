"""Module for registering models with the Django admin site."""
from django.contrib import admin

from .models import Email_verification, User, UserActivityLog, Department, Employee, Expense


class User_Admin(admin.ModelAdmin):
    """Admin configuration for the User model."""

    list_display = ["id", "username", "email", "name","phone_number","city" ,"photo", "email_verified", "role", "logged_in"]
    filter_horizontal = ()
    list_filter = ["role", "email_verified"]
    fieldsets = ()


admin.site.register(User, User_Admin)
admin.site.register(Email_verification) 
admin.site.register(UserActivityLog)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Expense)