from django.db import models

class Category(models.Model):
    #Name of the Category
    category_name = models.CharField(max_length=200)
    #Owner of the Category
    owner = models.ForeignKey('auth.User', related_name='categories')

    class Meta:
        ordering = ()

    def __str__(self):
        return self.category_name

class Property(models.Model):
    #Property type choices
    PROPERTY_TYPES = (
        ('S', 'String'),
        ('I', 'Integer'),
        ('D', 'Date'),
        ('P', 'Image'),
    )

    #Category that this property is related to
    category = models.ForeignKey('Category', related_name='properties')
    #Name of the property we're defining
    property_name = models.CharField(max_length=200)
    #Property type selected from the list above
    property_type = models.CharField(choices=PROPERTY_TYPES, max_length=1)


    class Meta:
        ordering = ()

    def __str__(self):
        return self.property_name

class Item(models.Model):
    #Category that the Item belongs to
    category = models.ForeignKey('Category', related_name='cagtegory')
    #Owner of the Item
    owner = models.ForeignKey('auth.User', related_name='items')
    #TODO: Let the user define the property to use as the identifier
    item_name = models.CharField(max_length=255)

    class Meta:
        ordering = ()


class PropertyItem(models.Model):
    #Property that we're defining the value of
    property = models.ForeignKey('Property', related_name='property')
    #Item that has this value
    item = models.ForeignKey('Item', related_name='item')
    #Value we're defining
    property_value = models.CharField(max_length=255)