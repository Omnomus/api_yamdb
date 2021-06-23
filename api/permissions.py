from rest_framework import permissions


class IsAuthorOrStaff(permissions.BasePermission):
    """
    Allow access only to staff or instance author.
    """
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user == obj.author
                or (request.user.is_moderator or request.user.is_admin))


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permission class for views: titles, genres, categories.
    """
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.auth and request.user.is_admin))


class IsOwner(permissions.BasePermission):
    """
    Allow access only to instance owner.
    """
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user == obj.owner)


class IsAdmin(permissions.BasePermission):
    """
    Allow access only to users with 'admin' role.
    """
    def has_permission(self, request, view):
        return (request.auth and request.user.is_admin)
