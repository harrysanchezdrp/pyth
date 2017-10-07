from django.db import models

class Product(models.Model):
    name = models.CharField(verbose_name=u'Name', max_length=32, unique=True)
    category = models.ForeignKey('Category')
    image = models.ImageField(upload_to='products', blank=True)
    description = models.TextField(verbose_name='Description', blank=True)


class Category(models.Model):
    name = models.CharField(verbose_name=u'Name', max_length=16, unique=True)

    def __str__(self):
        return self.name