from rest_framework import permissions
from rest_framework.exceptions import status

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or admins to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in ["GET", "PUT"]:
            return obj.owner == request.user or request.user.userprofile.is_admin
        return True
