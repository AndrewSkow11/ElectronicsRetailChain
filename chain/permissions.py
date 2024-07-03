from rest_framework.permissions import BasePermission


class IsActiveEmployee(BasePermission):
    """Настройка права доступа к API так, чтобы только активные
     сотрудники имели доступ к API."""

    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated
                and request.user.is_active)
