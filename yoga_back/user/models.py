from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import ugettext_lazy as _
# Create your models here.

SEX_CHOICES = [
    ('M', 'M'),
    ('F', 'F'),
]
class User(models.Model):
    first_name = models.CharField(_('Имя'), max_length=255, null=True, blank=True)
    last_name = models.CharField(_('Фамилия'), max_length=255, null=True, blank=True)
    image = models.ImageField(verbose_name='Фото профиля')
    sex = models.CharField(_('Пол'), max_length=1, choices=SEX_CHOICES)
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']
        
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Admin(models.Model):
    email = models.EmailField(verbose_name='Почта', max_length=255, unique=True)
    password = models.CharField(verbose_name='Почта', max_length=255)

    class Meta:
        verbose_name = 'Администратор'
        verbose_name_plural = 'Администраторы'
        ordering = ['id']
        
    def __str__(self):
        return self.email
