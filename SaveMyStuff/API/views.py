from API.models import Category
from API.serializers import *
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from API.permissions import *
from rest_framework.response import Response

#TODO: Setup Token Auth: http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #permission_classes = (IsOwner,)

    #Defining a custom get_queryset so that only the currently logged-in user's categories are returned
    #TODO: Fix the fact that I get a 500 error if I try to access the list view without being logged in. Should get a 401 Unauthorized
    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(owner=user)


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