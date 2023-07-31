from django.db import models
from django.contrib.auth.models import User


class ChatMessage(models.Model):
    """
    Модель для представления сообщения чата
    """

    # Поля
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=3000)
    message_html = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Строка для представления сообщения
        """

        return self.message