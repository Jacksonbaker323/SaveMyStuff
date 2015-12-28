from rest_framework import serializers
from API.models import Category, Property, Item, PropertyItem
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


class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    category = serializers.PrimaryKeyRelatedField(many=False, queryset=Category.objects.all(), read_only=False)

    class Meta:
        model = Item
        fields = ('id', 'owner', 'category', 'item_name')

class PropertyItemSerializer(serializers.ModelSerializer):
    #TOFIX: When creating a property item I get the following error: Cannot assign "6": "PropertyItem.item" must be a "Item" instance.
    item = serializers.ChoiceField(choices=Item.objects.values_list('id', 'item_name'))
    #Show all of the available properties
    #TODO: Restrict this to only the properties for the selected category
    property = serializers.PrimaryKeyRelatedField(many=False, queryset=Property.objects.all(), read_only=False)

    class Meta:
        model = PropertyItem
        fields = ('id', 'item', 'property', 'property_value')

