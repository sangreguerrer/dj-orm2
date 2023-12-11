from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    Category = models.ManyToManyField(Category, through="CategoryArticle")

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']


    def __str__(self):
        return self.title


class CategoryArticle(models.Model):
    Article = models.ForeignKey(Article, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False, verbose_name='Основной раздел')








