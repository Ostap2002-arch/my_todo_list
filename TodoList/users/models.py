from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    photo = models.ImageField(verbose_name='Фотография', upload_to='users/%Y/%m/%d/', blank=True, null=True)
    about = models.CharField(verbose_name='О себе', max_length=256, blank=True, null=True)
    birthday = models.DateTimeField(verbose_name='День рождения', blank=True, null=True)
