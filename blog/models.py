from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Post(models.Model):
    # мета опции
    class Meta:
        verbose_name = 'Добавить пост'
        verbose_name_plural = 'Добавить посты'

    title = models.CharField(max_length=200, help_text="не более 200 символов", db_index=True)
    content = models.TextField(max_length=5000, blank=True, null=True, help_text="не более 5000 символов")
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50)


# Вместо объекта возвращает title, можно выполнить при помощи декоратора
    def __str__(self):
        return self.title

