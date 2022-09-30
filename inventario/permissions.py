from rest_framework import permissions


class IsUserAlmacen(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='Almacen'):
            return True
        return False
