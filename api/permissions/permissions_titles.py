from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permission class for views: titles, genres, categories.
    """
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.auth and request.user.role == 'admin'))
