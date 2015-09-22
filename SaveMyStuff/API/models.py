from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name

class Category(models.Model):
    category_of_owner = models.ForeignKey(User)
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class Property(models.Model):
    property_of_category = models.ForeignKey(Category)
    property_name = models.CharField(max_length=200)

    def __str__(self):
        return self.property_name

class PropertyTypes(models.Model):
    #Property types
    TYPES = ('String', 'Integer', 'Date', 'Currency', 'Image')
    property_type_of_property = models.ForeignKey(Property)
    property_type_name = models.CharField(max_length=50, choices=TYPES)

    def __str__(self):
        return self.property_type_name

'''
class Item(models.Model):
    item_name = models.CharField(max_length=200)

class ItemProperty(models.Model):
    item_property_value = models.CharField(max_length=200)
'''
