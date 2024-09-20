"""This module provides enums for user dataset role."""
from enum import Enum


class RoleEnum(Enum):
    """Provides enums for user roles."""

    User = "user"
    Admin = "admin"
    Executive = "executive"
