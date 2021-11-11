from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUser(BasePermission):
    """
    Allows access only to Super admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsStaffOrReadOnly(BasePermission):
    """
    The request is authenticated and staff as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or request.user and request.user.is_staff
        )


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return bool(
            # get access to super user
            request.user.is_authenticated
            and request.user.is_superuser
            or
            # get access to
            obj.author == request.user
        )


class StaffReadOnlyOrSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(
            # user be super one.
            request.user
            and request.user.is_authenticated
            and request.user.is_superuser
            or
            # read only for staff user.
            request.method in SAFE_METHODS
            and request.user
            and request.user.is_authenticated
            and request.user.is_staff
        )
