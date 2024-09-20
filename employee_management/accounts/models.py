"""Models for user."""
import uuid
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from .verification_email import send_verification_email
from .enums.role_enum import RoleEnum
from django.db import models
from django.conf import settings
from django.utils import timezone

class User(AbstractUser):
    """Provide fields for User Model."""

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    phone_number = models.BigIntegerField(
        blank=True, help_text="User phone number", null=True
    )
    city = models.CharField(max_length=150)
    photo = models.ImageField(upload_to="media/profile")
    role = models.CharField(
        choices=((role.value, role.name) for role in RoleEnum),
        help_text="Choice for role.",
        max_length=20,
    )

    USERNAME_FIELD = "email"  # e.g: "username", "email"
    EMAIL_FIELD = "email"
    logged_in = models.BooleanField(
        default=False, help_text="Flag to define user is login"
    )
    email_verified = models.BooleanField(
        help_text="Flag to define is email is verified", default=False
    )
    REQUIRED_FIELDS = ["username"]


class Email_verification(models.Model):
    """Define class for email verification process."""

    user = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, help_text="Attach user model"
    )
    token = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, help_text="Unique token"
    )
    verified = models.BooleanField(default=False, help_text="Verification field")
    expiration_time = models.DateTimeField(
        help_text="Expiration time for the verification link", null=True, blank=True
    )

    def resend_email_verification(user: get_user_model) -> None:
        """Resend email to verify."""
        email_obj = Email_verification.objects.create(user=user)
        send_verification_email(user=user, token=email_obj.token)
        email_obj.expiration_time = timezone.now() + timedelta(minutes=3)
        email_obj.save()


class UserActivityLog(models.Model):
    """Model to track user login activity and other actions."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action = models.CharField(max_length=255, help_text="Activity performed by the user")
    timestamp = models.DateTimeField(default=timezone.now, help_text="Time when the activity occurred")

    def __str__(self):
        return f"{self.user.email} - {self.action} at {self.timestamp}"

class Department(models.Model):
    """Model to represent a department."""
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    """Model to represent an employee."""
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Expense(models.Model):
    """Model to represent an expense."""
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"{self.description} - {self.amount} on {self.date}"
