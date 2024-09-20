"""This module provides urls to views."""
from django.urls import path
from .views.login_view import LoginView
from .views.register_view import RegisterView
from .views.resend_email_view import ResendEmailVerificationView
from .views.verify_email_view import VerifyEmailView
from .views.management_views import EmployeeManagementView, DepartmentManagementView, ExpenseManagementView
from .views.dashboard_views import UserDashboardView, AdminDashboardView

urlpatterns = [
    # Authentication paths
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("verify/<token>/", VerifyEmailView.as_view(), name="verify_email"),
    path("resend-email/", ResendEmailVerificationView.as_view(), name="resend_email"),

    # Management paths
    path('employees/', EmployeeManagementView.as_view(), name='employee_management'),
    path('departments/', DepartmentManagementView.as_view(), name='department_management'),
    path('expenses/', ExpenseManagementView.as_view(), name='expense_management'),

    # Dashboard paths
    path('dashboard/user/', UserDashboardView.as_view(), name='user_dashboard'),
    path('dashboard/admin/', AdminDashboardView.as_view(), name='admin_dashboard'),
]
