from rest_framework import serializers
from API.models import Category
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        #Point the serializer at the model definition and list the fields that you want to be displayed
        model = Category
        fields = ('id', 'category_name', 'owner')
        owner = serializers.ReadOnlyField(source='owner.username')

class UserSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'categories')
