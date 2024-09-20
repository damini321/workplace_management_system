"""This module define resend email serializer utility."""
from rest_framework import serializers


class ResendActivationEmailSerializer(serializers.Serializer):
    """Define serializer for resend activation email."""

    email = serializers.EmailField(max_length=300, allow_null=False, allow_blank=False)
