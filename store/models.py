
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

    # def get_absolute_url(self):
    #     return reverse("", kwargs={"pk": self.pk})

    def get_absolute_url_for_basket(self):
        return reverse("basket_add", kwargs={"slug": self.slug})
    
    
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# class Basket(models.Model):
#     user = models.ForeignKey(
#         "users.User", related_name="basket_products", on_delete=models.CASCADE
#     )
#     product = models.ForeignKey("store.Product", on_delete=models.CASCADE)
#     quantity = models.PositiveSmallIntegerField()
#     create_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user} -- {self.product}"
