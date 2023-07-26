from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.


class Post(models.Model):
    # мета опции
    class Meta:
        verbose_name = 'Добавить пост'
        verbose_name_plural = 'Добавить посты'

    title = models.CharField(max_length=200, help_text="не более 200 символов", db_index=True)
    #content = models.TextField(max_length=5000, blank=True, null=True, help_text="не более 5000 символов")
    content = RichTextField(blank=True, null=True, help_text="не более 5000 символов", max_length=5000)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50)
    likes = models.ManyToManyField(User, related_name= 'postcomment', blank=True)
    reply = models.ForeignKey('self', null=True, related_name='reply_ok', on_delete=models.CASCADE)

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={'pk': self.pk})

# Вместо объекта возвращает title, можно выполнить при помощи декоратора
    def __str__(self):
        return self.title

