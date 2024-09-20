"""Define user common fields serializer."""
from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    """Define user common field serializer."""

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "phone_number"]
        read_only_fields = ["email"]
