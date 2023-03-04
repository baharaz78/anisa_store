from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)


class Category(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children"
    )

    def __str__(self):
        return self.name

    # @property
    # def capitalized_name(self):
    #     return self.name.title()


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    discount = models.PositiveIntegerField(
        validators=[MaxValueValidator(100)], default=0
    )
    count = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        null=True,
        blank=True,
    )
    is_available = models.BooleanField(default=True)
    product = models.ManyToManyField(Tag, related_name="products")


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.discount > 50:
            raise ValueError("Bad Discount")

        return super().save(*args, **kwargs)


class Comment(models.Model):
    body = models.TextField()
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="comments"
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="replies",
        null=True,
        default=None,
    )
    date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="users")

    def __str__(self):
        return self.product


class Rank(models.Model):
    product_rank = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)], default=0
    )
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="ranking"
    )
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.product
