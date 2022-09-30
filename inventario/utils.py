from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied


def permission_required(perm):
    """
    Override default permission required decorator
    :param perm: permissions tuple or str
    :return: True if success, otherwise False
    """
    def check_perms(user):
        if user.has_perms(perm) or user.is_superuser:
            return True
        else:
            raise PermissionDenied

    return user_passes_test(check_perms)
