# Workplace Management System

## Overview
The Workplace Management System is a web application built with Django and Django REST Framework. It provides functionalities for user registration, login, dashboards for different roles (User, Admin, Executive), and management of employees, departments, and expenses.

## Features

### User Registration
- Fields: Username, Email, Password, Name, Phone, City, Profile Photo, Role (User/Admin/Executive).
- OTP verification upon registration.

### Login
- Fields: Username/Email, Password.
- Role-based redirection to respective dashboards.

### Dashboards
- **User Dashboard**: Displays user-specific information, activity logs, and engagement metrics.
- **Admin Dashboard**: Provides user management, user growth charts, role distribution, and system metrics.
- **Executive Dashboard**: Displays employee management and department-wise metrics.

### Management
- **Employee Management**: Add and display employee details.
- **Department Management**: Add and display department details.
- **Expense Management**: Add and display expenses.

### Notifications
- Notifications for user registrations, logins, activity logs, and more.

### Activity Logging
- Logs all user activities with timestamps.

## Technologies Used
- Python
- Django
- Django REST Framework
- PostgreSQL (or any other database you are using)
- Bootstrap (for front-end design)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/damini321/workplace_management_system
2. Navigate to the project directory:
   ```bash
   cd workplace_management_system
3. Set up a virtual environment:
   ```bash
   python -m venv venv
4. Activate the virtual environment:
   ```bash
   venv\Scripts\activate
5. Install the required packages:
   ```bash
   pip install -r requirements.txt
6. Set up environment variables (e.g., in a .env file):
   ```bash
   EMAIL_HOST_USER=your_email@example.com
   EMAIL_HOST_PASSWORD=your_password
7. Apply migrations:
   ```bash
   python manage.py migrate
8. Run the development server:
   ```bash
   python manage.py runserver

### Usage
Visit http://localhost:8000/auth/register/ to register and http://localhost:8000/auth/login/ to log in.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
