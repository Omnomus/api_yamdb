from rest_framework import permissions


class SafeMethods(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author


class IsAuthAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.auth and request.user.role == 'admin')


class IsStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == ('moderator' or 'admin')


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
