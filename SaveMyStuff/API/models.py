from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.User', related_name='categories')

    class Meta:
        ordering = ()

    def __str__(self):
        return self.category_name

class Property(models.Model):
    PROPERTY_TYPES = (
        ('S', 'String'),
        ('I', 'Integer'),
        ('D', 'Date'),
        ('P', 'Image'),
    )

    category = models.ForeignKey('Category', related_name='properties')
    property_name = models.CharField(max_length=200)
    property_type = models.CharField(choices=PROPERTY_TYPES, max_length=1)

    class Meta:
        ordering = ()

    def __str__(self):
        return self.property_name
