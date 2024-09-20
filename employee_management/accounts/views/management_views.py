from django.contrib import messages
from django.shortcuts import redirect, render
from accounts.models import Employee, Department, Expense
from accounts.forms import EmployeeForm, DepartmentForm, ExpenseForm
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView

class EmployeeManagementView(APIView):
    """Manage employees."""
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        employees = Employee.objects.all()
        form = EmployeeForm()
        return render(request, 'email/employee_management.html', {'employees': employees, 'form': form})

    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee added successfully!')
            return redirect('employee_management')
        return render(request, 'email/employee_management.html', {'form': form})

class DepartmentManagementView(APIView):
    """Manage departments."""
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        departments = Department.objects.all()
        form = DepartmentForm()
        return render(request, 'email/department_management.html', {'departments': departments, 'form': form})

    def post(self, request):
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department added successfully!')
            return redirect('department_management')
        return render(request, 'email/department_management.html', {'form': form})

class ExpenseManagementView(APIView):
    """Manage expenses."""
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        expenses = Expense.objects.all()
        form = ExpenseForm()
        return render(request, 'email/expense_management.html', {'expenses': expenses, 'form': form})

    def post(self, request):
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense added successfully!')
            return redirect('expense_management')
        return render(request, 'email/expense_management.html', {'form': form})
