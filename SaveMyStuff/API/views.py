
from API.models import Category, Property, Item, PropertyItem
from API.serializers import *

from django.contrib.auth.models import User
from rest_framework import viewsets

#TODO: Setup Token Auth: http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    #Only returns the categories that the user has access to
    #TODO: Determine the best way to create a class that handles this automatically across different models
    def get_queryset(self):
        return self.request.user.categories.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PropertyItemViewSet(viewsets.ModelViewSet):
    queryset = PropertyItem.objects.all()
    serializer_class = PropertyItemSerializer
