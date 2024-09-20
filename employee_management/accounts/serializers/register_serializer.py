"""This module define register serializer utility."""
from datetime import timedelta

import django.contrib.auth.password_validation as validators
from django.core import exceptions
from django.utils import timezone
from accounts.verification_email import send_verification_email
from rest_framework import serializers
from accounts.models import Email_verification, User


class RegisterUserSerializer(serializers.ModelSerializer):
    """Provide models and fields."""

    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = (
            "email",
            "username",
            "password",
            "password2",
            "name",
            "phone_number",
            "city",
            "photo",
            "role",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs: dict) -> dict:
        """Validate password with first password."""
        password = attrs["password"]
        password2 = attrs.pop("password2")
        errors = {}
        try:
            if password != password2:
                raise serializers.ValidationError("Passwords do not match.")
            validators.validate_password(password=password)
        except exceptions.ValidationError as e:
            errors["password"] = list(e.messages)
        if errors:
            raise serializers.ValidationError(errors)

        return attrs

    def create(self, validated_data: dict) -> User:
        """Create user with email and password."""
        send_email = validated_data.pop("send_email", False)
        user = User.objects.create_user(**validated_data)

        if send_email:
            self.create_email_verification(user)
        return user

    def create_email_verification(sender, instance: Email_verification) -> None:
        """Create email verification logic."""
        email_obj = Email_verification.objects.create(user=instance)
        send_verification_email(user=instance, token=email_obj.token)
        email_obj.expiration_time = timezone.now() + timedelta(minutes=90)
        email_obj.save()
