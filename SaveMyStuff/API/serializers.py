from rest_framework import serializers
from API.models import Category, Property
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'categories')


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('id', 'property_name', 'property_type', 'category')


class CategorySerializer(serializers.ModelSerializer):
    #Setting the definition of the "Owner" field used below and making it read only
    owner = serializers.ReadOnlyField(source='owner.id')
    properties = PropertySerializer(many=True, read_only=True)

    class Meta:
        #Point the serializer at the model definition and list the fields that you want to be displayed
        model = Category
        fields = ('id', 'category_name', 'owner', 'properties')



