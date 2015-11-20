from rest_framework import permissions

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        #NOTE: This function IS NOT HIT when the Category List is displayed. Might need to define a different function to control what objects a user sees
        return obj.owner == request.user

