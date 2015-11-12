from rest_framework import serializers
from API.models import Category


#Fully expanded class
'''
class CategorySerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    category_name = serializers.CharField(required=True, allow_blank=False, max_length=200)

    def create(self, validated_data):
        #Create and return a Category class with the validated data
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #Update an existing Category instance
        instance.category_name = validated_data.get('category_name', instance.category_name)
        instance.save()
        return instance
'''

#Minimized class

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        #Adding a trailing ',' because Python only recognizes this as a tuple if there are multiple items in it
        fields = ('id', 'category_name')