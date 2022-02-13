from app.internal.models.admin_user import AdminUser
from django.db import models


class User(models.Model):
    tg_id = models.PositiveBigIntegerField(primary_key=True)
    username = models.CharField(max_length=32, null=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=16, unique=True, blank=True)

    def __str__(self):
        return f'@{self.username}' if self.username is not None else f'{self.tg_id}'
