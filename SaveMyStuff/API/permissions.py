from rest_framework import permissions

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        #NOTE: This function IS NOT HIT when the Category List is displayed. Might need to define a different function to control what objects a user sees
        print("Owner: " + str(obj.owner))
        print("Requestor: " + str(request.user))
        return obj.owner == request.user

http://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/