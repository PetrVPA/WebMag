from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Category", help_text="Введите название категории"
    )
    description = models.TextField(
        verbose_name="Category product", help_text="Введите писание категории"
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["title"]

class Product(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Product title",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        verbose_name="Description product", help_text="Описание товара"
    )
    images = models.ImageField(
        upload_to="products/photo",
        blank=True,
        null=True,
        verbose_name="Image Product",
        help_text="Загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Category Product",
        help_text="Введите категорию продукта",
        related_name="products",
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=False,
        null=False,
        verbose_name="Price Product",
        help_text="Введите цену продукта",
    )
    created_at = models.DateField(
        blank=False,
        null=False,
        verbose_name="Date of creation Product",
        help_text="Введите дату создания продукта",
    )
    updated_at = models.DateField(
        blank=False,
        null=False,
        verbose_name="Date of modification Product",
        help_text="Введите дату изменения продукта",
    )

    def __str__(self):
        return f"{self.title}, {self.category}, {self.price}"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["title"]
