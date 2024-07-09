from rest_framework import permissions


class IsModer(permissions.BasePermission):
    massage = "Эти права Вам не доступны, Вы не являетесь модератором."

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moders").exists()


class IsOwner(permissions.BasePermission):
    massage = "У нас нет прав доступа."

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
