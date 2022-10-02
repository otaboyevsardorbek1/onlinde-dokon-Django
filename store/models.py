from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=60)
    photo = models.ImageField(upload_to="category_image/%Y/%m/%d")

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=60)
    category = models.ForeignKey(
        "store.Category", related_name="subcategory", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to="product_image/%Y/%m/%d")
    product = models.ForeignKey(
        "store.Product", related_name="images", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.product.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', null=True)
    description = models.CharField(max_length=255)
    price = models.PositiveSmallIntegerField(default=0)
    image = models.ImageField(upload_to="product_image/%Y/%m/%d", null=True)
    quantity = models.PositiveSmallIntegerField()
    
    subcategory = models.ForeignKey(
        "store.SubCategory",
        related_name="products",
        on_delete=models.CASCADE,
        null=True,
    )

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    def get_absolute_url_for_modal(self):
        return reverse("detail_window", kwargs={"slug": self.slug})

    def get_absolute_url_for_add_to_basket(self):
        return reverse("basket_add", kwargs={"slug": self.slug})

    def get_absolute_url_for_remove_from_basket(self):
        return reverse("basket_remove", kwargs={"slug": self.slug})
    
    def get_absolute_url_for_remove_count_from_basket(self):
        return reverse("basket_remove_count", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name



class Order(models.Model):
    ordered_by = models.ForeignKey("users.User", on_delete=models.PROTECT, related_name='orders', blank=True)
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    total_price = models.PositiveIntegerField()

class OrderItem(models.Model):
    order = models.ForeignKey('store.Order', on_delete=models.PROTECT, related_name='items')
    product = models.ForeignKey("store.Product", on_delete=models.PROTECT, related_name="items")
    quantity = models.PositiveSmallIntegerField()
    total_price = models.PositiveIntegerField()