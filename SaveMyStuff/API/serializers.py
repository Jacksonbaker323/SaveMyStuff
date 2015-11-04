from rest_framework import serializers
from API import models

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