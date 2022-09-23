from django.contrib import admin

from .models import Category, SubCategory, Product, ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", 'photo']

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", 'category']

class PostImageAdmin(admin.StackedInline):
    model = ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug",'price', 'quantity', 'subcategory']
    inlines = [PostImageAdmin]

@admin.register(ProductImage)
class ProductImageyAdmin(admin.ModelAdmin):
    list_display = ["id", "image", 'product']
