"""Module containing serializers for user login functionality."""
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token
from accounts.enums.role_enum import RoleEnum
from accounts.models import User


class UserLoginSerializer(TokenObtainPairSerializer):
    """Define user login flow."""

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
    username_field = User.EMAIL_FIELD

    @classmethod
    def get_token(cls, user: User) -> Token:
        """Add role to JWT token created."""
        token = super().get_token(user)
        token["role"] = user.role
        return token

    def validate(self, data: dict) -> dict:
        """Validate the user data."""
        email = data.get("email")
        password = data.get("password")
        self.validate_email_and_password(email, password)
        user = self.get_user_by_email(email)
        self.check_user_existence(user)
        self.check_email_verification(user)
        validate_data = super().validate(data)
        validate_data['user'] = user
        self.update_user_login_status(user)
        return validate_data

    def validate_email_and_password(self, email: str, password: str) -> None:
        """Validate email and password presence."""
        if email is None:
            raise serializers.ValidationError("An email address is required to log in.")
        if password is None:
            raise serializers.ValidationError("A password is required to log in.")

    def get_user_by_email(self, email: str) -> User:
        """Get user by email."""
        return User.objects.filter(email=email).first()

    def check_user_existence(self, user: User) -> None:
        """Check if user exists."""
        if not user:
            raise serializers.ValidationError("User does not exist")

    def check_email_verification(self, user: User) -> None:
        """Check if user's email is verified."""
        if not user.email_verified:
            raise serializers.ValidationError("Unverified account")

    def update_user_login_status(self, user: User) -> None:
        """Update user's login status."""
        user.logged_in = True
        user.save()
