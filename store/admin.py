from django.contrib import admin

from .models import Category, SubCategory, Product, ProductImage, Basket

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", 'photo']

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", 'category']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", 'price', 'quantity', 'subcategory']

@admin.register(ProductImage)
class ProductImageyAdmin(admin.ModelAdmin):
    list_display = ["id", "image", 'product']

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ["id", "user", 'product']
    