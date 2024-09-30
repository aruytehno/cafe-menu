from django.contrib import admin
from django.utils.html import format_html
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_price', 'item_in_stock', 'display_image')
    fields = ('item_name', 'item_category', 'item_ingredients', 'item_mass', 'item_price', 'item_in_stock', 'item_image', 'display_image')
    readonly_fields = ('display_image',)  # Чтобы сделать поле только для чтения

    def display_image(self, obj):
        if obj.item_image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.item_image.url)
        return "Нет изображения"
    display_image.short_description = 'Изображение'  # Заголовок для поля

    list_filter = ('item_category',)
    search_fields = ('item_name',)

admin.site.register(Product, ProductAdmin)
