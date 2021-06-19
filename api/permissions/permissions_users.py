from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """Allows access only to users with 'admin' role."""
    def has_permission(self, request, view):
        if not request.user.is_anonymous:
            return request.user.role == 'admin'
        return False
