from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Прошёл активацию')
    send_messages = models.BooleanField(default=True, verbose_name='Подписка на комментарии')

    class Meta(AbstractUser.Meta):
        pass
