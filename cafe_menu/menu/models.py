from random import choices

from django.db import models


class Product(models.Model):
    item_category = models.CharField(max_length=50, verbose_name='Категория')
    item_name = models.CharField(max_length=100, verbose_name='Наименование')
    item_ingredients = models.TextField(max_length=500, verbose_name='Ингридиенты', blank=True)
    item_mass = models.CharField(max_length=50, verbose_name='Масса/объём', blank=True)
    item_price = models.IntegerField(verbose_name='Цена')
    item_in_stock = models.BooleanField(verbose_name='В наличии')

    class Meta:
        verbose_name = u'товар'
        verbose_name_plural = u'Товары'

    def __str__(self):
        return self.item_name
