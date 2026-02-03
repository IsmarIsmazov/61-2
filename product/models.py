from django.db import models

# Create your models here.
# ORM Object Relational Mapping

# OneToMany - одна категория - много продуктов
# ManyToMany - много Тэг - много продуктов
# OneToOne - один Пользователь - одна Профиль

# FK - Foreign Key


class Category(models.Model):  # 0+, 6+
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="products/")
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.price}"
