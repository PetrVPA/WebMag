from django.db import models

class Blog(models.Model):
    title_article = models.CharField(
        max_length=100,
        verbose_name="Product title",
        help_text="Название статьи",
    )
    content = models.TextField(
        verbose_name="Content article", help_text="Содержимое статьи"
    )
    preview = models.ImageField(
        upload_to="blogs/photo",
        blank=True,
        null=True,
        verbose_name="Image article",
        help_text="Загрузите изображение статьи",
    )

    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Date of creation article",
        help_text="Дату создания статьи",
    )
    publication_indicator = models.BooleanField(
        default=False,
        blank=True,
        null=True,
        verbose_name="Publication indicator",
        help_text="Признак публикации",
    )

    number_views = models.IntegerField(
        default=0,
        blank=True,
        null=True,
        verbose_name="Number of views",
        help_text="Количество просмотров",
    )

    def __str__(self):
        return f"{self.title_article}, {self.preview}, {self.price}"

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ["title_article"]
