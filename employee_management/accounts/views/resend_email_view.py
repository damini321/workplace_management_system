"""This module provides resend email for user."""

from typing import Any

from django.http import HttpRequest
from rest_framework import generics, status
from rest_framework.response import Response
from accounts.models import Email_verification, User
from accounts.serializers.resend_email_serializer import ResendActivationEmailSerializer


class ResendEmailVerificationView(generics.GenericAPIView):
    """Provides resend email verification process."""

    serializer_class = ResendActivationEmailSerializer

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> Response:
        """Resend Email verification process."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        try:
            user = User.objects.get(email=email)
            Email_verification.resend_email_verification(user)
            return Response(
                {"detail": "Activation email resent successfully."},
                status=status.HTTP_200_OK,
            )
        except User.DoesNotExist:
            return Response(
                {"detail": "User with this email does not exist."},
                status=status.HTTP_400_BAD_REQUEST,
            )
