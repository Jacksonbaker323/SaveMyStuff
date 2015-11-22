from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.User', related_name='categories')

    class Meta:
        ordering = ()

    def __str__(self):
        return self.category_name

class Property(models.Model):
    PROPERTY_LIST = (
        ('S', 'String'),
        ('I', 'Int'),
        ('D', 'Date'),
        ('C', 'Currency'),
    )
    property_name = models.CharField(max_length=200)
    property_type = models.CharField(max_length=1, choices=PROPERTY_LIST)
    category = models.ForeignKey('Category', related_name='category')

    class Meta:
        ordering = ()

    def __str__(self):
        return self.property_name