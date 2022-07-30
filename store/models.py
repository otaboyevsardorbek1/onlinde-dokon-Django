from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=60)
    photo = models.ImageField(upload_to="category_image/%Y/%m/%d")


class SubCategory(models.Model):
    name = models.CharField(max_length=60)
    category = models.ForeignKey(
        "store.Category", related_name="subcategory", on_delete=models.CASCADE
    )


class ProductImage(models.Model):
    image = models.ImageField(upload_to="product_image/%Y/%m/%d")
    product = models.ForeignKey(
        "store.Product", related_name="images", on_delete=models.CASCADE
    )


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.PositiveSmallIntegerField(default=0)
    quantity = models.PositiveSmallIntegerField()
