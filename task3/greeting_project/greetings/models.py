from django.db import models


class Greeting(models.Model):
    """Модель для хранения имён пользователей, отправивших форму."""

    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
