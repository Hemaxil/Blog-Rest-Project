from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    message= 'You are not the owner'

    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        print(obj.user,request.user)
        return obj.user==request.user