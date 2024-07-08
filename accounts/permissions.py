from rest_framework import permissions


class IsSelfOrReadonly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.methods in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
