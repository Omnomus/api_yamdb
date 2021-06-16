from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    """Custom permission to allow moderators to delete an object."""
    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE' and request.user.role == 'moderator':
            return True
