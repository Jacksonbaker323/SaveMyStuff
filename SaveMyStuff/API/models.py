from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.User', related_name='categories')

    class Meta:
        ordering = ()

    def __str__(self):
        return self.category_name

class Property(models.Model):
    property_name = models.CharField(max_length=200)


    class Meta:
        ordering = ()

    def __str__(self):
        return self.property_name