from rest_framework import permissions
from django.contrib.auth.models import User


class IsStaffOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow staffs of NCLab to edit it.
    """

    def has_staff_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        try:
        	user = User.objects.get(user=request.user)
        except User.DoesNotExist:
        	return False
        return user.is_staff
