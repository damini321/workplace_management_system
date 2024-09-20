# """This module provides registration for user."""

from django.contrib import messages
from django.shortcuts import render, redirect
from rest_framework import generics
from accounts.forms import RegisterUserForm
from accounts.models import Email_verification  # Make sure to import your Email_verification model
from accounts.verification_email import send_verification_email  # Import the function to send verification email
from django.utils import timezone
from datetime import timedelta

class RegisterView(generics.GenericAPIView):
    """Define user registration flow."""
    
    def get(self, request):
        form = RegisterUserForm()
        return render(request, 'email/register.html', {'form': form})

    def post(self, request):
        form = RegisterUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()

            # Create an email verification entry
            email_verification = Email_verification.objects.create(user=user)
            email_verification.expiration_time = timezone.now() + timedelta(minutes=15)  # Set expiration time to 15 minutes from now
            email_verification.save()  # Save the changes
            send_verification_email(user=user, token=email_verification.token)

            messages.success(request, "Registration successful. Please check your email to verify your account.")
            return redirect('login')
        
        return render(request, 'email/register.html', {'form': form})
