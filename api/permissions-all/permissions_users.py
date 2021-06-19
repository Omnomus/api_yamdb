from rest_framework import permissions

# class IsAdmin(permissions.BasePermission):
#     """Custom permission to allow moderators to delete an object."""
#     def has_object_permission(self, request, view, obj):
#         if not request.user.is_admin:
#             return False
#         return True


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user == obj.owner)
