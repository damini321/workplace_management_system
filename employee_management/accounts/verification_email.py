"""Define verification email process."""
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from employee_management.settings import EMAIL_HOST_USER, SITE_DOMAIN


def send_verification_email(user: get_user_model, token: str) -> None:
    """Send email to user to verify."""
    verification_url = f"{SITE_DOMAIN}/auth/verify/{token}"
    subject = "Verify your email address"
    html_message = render_to_string(
        "email/email_verification_template.html", {"verification_url": verification_url}
    )
    plain_message = strip_tags(html_message)

    sender_email = EMAIL_HOST_USER
    recipient_email = user.email

    send_mail(
        subject,
        plain_message,
        sender_email,
        [recipient_email],
        html_message=html_message,
    )
