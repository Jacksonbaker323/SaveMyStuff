from API.models import Category
from API.serializers import *
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from API.permissions import *

#TODO: Setup Token Auth: http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication



#TODO: Determine why I can see things that my user did not create in the list view
#TODO CONT: Ideally I'd be able to only show a list of the current users categories
#TODO TOREAD: http://www.django-rest-framework.org/api-guide/permissions/

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsOwner,)

    #Add the user to any 'save' request
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsOwner,)



###--------- User Classes -------------
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer