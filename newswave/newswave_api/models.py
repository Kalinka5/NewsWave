from django.db import models


class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.title


class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self) -> str:
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    news_name = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.image.name

