from django.db import models

class Product(models.Model):
    item_category = models.CharField(max_length=50, verbose_name='Категория')
    item_name = models.CharField(max_length=100, verbose_name='Наименование')
    item_ingredients = models.TextField(max_length=500, verbose_name='Ингредиенты', blank=True)
    item_mass = models.CharField(max_length=50, verbose_name='Масса/объём', blank=True)
    item_price = models.IntegerField(verbose_name='Цена')
    item_in_stock = models.BooleanField(verbose_name='В наличии')
    item_image = models.ImageField(upload_to='products/', verbose_name='Изображение', blank=True, null=True)  # Добавьте это поле

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.item_name
