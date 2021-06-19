from rest_framework import permissions


class IsAuthorOrStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user == obj.author
                or request.user.role == ('moderator' or 'admin'))


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permission class for views: titles, genres, categories.
    """
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.auth and request.user.role == 'admin'))


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user == obj.owner)


class IsAdmin(permissions.BasePermission):
    """
    Allows access only to users with 'admin' role.
    """
    def has_permission(self, request, view):
        return (request.auth and request.user.role == 'admin')