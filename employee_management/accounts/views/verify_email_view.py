"""This module provides verify email for user."""

from django.http import HttpRequest
from django.shortcuts import render
from django.utils import timezone
from django.views import View
from rest_framework import status
from accounts.models import Email_verification
from employee_management.settings import SITE_DOMAIN


class VerifyEmailView(View):
    """User email verification process."""

    template_already_verified = "email/already_verified.html"
    template_verification_failed = "email/email_verification_failed.html"
    template_email_verified = "email/email_verified.html"
    template_user_not_exists = "email/user_not_exists.html"

    def get(self, request: HttpRequest, token: str) -> str:
        """Verify email."""
        try:
            verification_record = Email_verification.objects.get(token=token)
            if verification_record.verified:
                return render(
                    request,
                    self.template_already_verified,
                    status=status.HTTP_208_ALREADY_REPORTED,
                )
            if verification_record.expiration_time is None or verification_record.expiration_time < timezone.now():
                context = {
                    "user_email": verification_record.user.email,
                    "SITE_DOMAIN": SITE_DOMAIN,
                }
                return render(
                    request,
                    self.template_verification_failed,
                    context=context,
                    status=status.HTTP_400_BAD_REQUEST,
                )

            verification_record.user.email_verified = True
            verification_record.user.save()
            verification_record.verified = True
            verification_record.save()
            return render(
                request, self.template_email_verified, status=status.HTTP_200_OK
            )
        except Email_verification.DoesNotExist:
            context = {
                "user_email": verification_record.user.email,
                "SITE_DOMAIN": SITE_DOMAIN,
            }
            return render(
                request,
                self.template_user_not_exists,
                context=context,
                status=status.HTTP_404_NOT_FOUND,
            )
