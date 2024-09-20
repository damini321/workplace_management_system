from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from accounts.models import UserActivityLog
from datetime import timedelta
from django.utils import timezone
from accounts.models import User
from django.db import models

class UserDashboardView(APIView):
    """Display user-specific data on the dashboard."""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        # Fetch activity logs
        activity_logs = UserActivityLog.objects.filter(user=user).order_by('-timestamp')
        
        recent_activities = activity_logs.filter(action__in=['login', 'logout'])[:10]
        
        # Example of calculating login frequency over the past 30 days
        login_logs = activity_logs.filter(action='login', timestamp__gte=timezone.now() - timedelta(days=30)).count()
        
        context = {
            'user': user,
            'activity_logs': activity_logs,
            'login_frequency': login_logs,
            'recent_activities': recent_activities,
        }
        return render(request, 'email/dashboard.html', context)

class AdminDashboardView(APIView):
    """Display admin-specific data on the dashboard."""
    #permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        # Fetch all users and other data
        users = User.objects.filter(is_superuser=False)
        user_growth = users.filter(date_joined__gte=timezone.now() - timedelta(days=30)).count()
        role_distribution = users.values('role').annotate(count=models.Count('role'))

        context = {
            'users': users,
            'user_growth': user_growth,
            'role_distribution': role_distribution,
        }
        return render(request, 'email/admin_dashboard.html', context)
