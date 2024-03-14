from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return True
        return False


class IsModerator(BasePermission):

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False