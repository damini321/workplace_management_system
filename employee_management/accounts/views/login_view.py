from django.http import HttpRequest
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.serializers.login_serializer import UserLoginSerializer

class LoginView(TokenObtainPairView):
    """Logic process for user."""
    serializer_class = UserLoginSerializer

    def get(self, request: HttpRequest) -> Response:
        """Render the login page."""
        return render(request, 'email/login.html')

    def post(self, request: HttpRequest) -> Response:
        """Get user data and perform validations."""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # Get the validated data
            validated_data = serializer.validated_data
            
            # Prepare the response data
            response_data = {
                "access": validated_data['access'],
                "refresh": validated_data['refresh'],
                "user": {
                    "id": validated_data['user'].id,
                    "email": validated_data['user'].email,
                    "role": validated_data['user'].role,
                    
                }
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
