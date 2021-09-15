from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

WORKOUT_LEVELS = (
    ('Простой', 'Простой'),
    ('Средний', 'Средний'),
    ('Продвинутый', 'Продвинутый'),
)
SEX_CHOICES = [
    ('M', 'M', 'U'),
    ('F', 'F', 'U'),
]

class Sex(models.Model):
    name = models.CharField(verbose_name='Пол', max_length=1)
    
class Level(models.Model):
    name = models.CharField(verbose_name='Уровень сложности', max_length=15)
class Day(models.Model):
    name = models.CharField(verbose_name='День недели', max_length=15)

class Trouble(models.Model):
    name = models.CharField(verbose_name=_('Название'), max_length=255, unique=True)
    image = models.ImageField(verbose_name=_('Превью'), null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Проблема')
        verbose_name_plural = _('Проблемы')
        ordering = ['id']

class Workout(models.Model):
    name = models.CharField(verbose_name=_('Название'), max_length=255)
    video = models.FileField(verbose_name=_('Видео'))
    duration = models.CharField(verbose_name=_('Длительность'), max_length=255)
    periodicity = models.ManyToManyField(Day, blank=True, related_name='workout_day')
    level = models.ManyToManyField(Level, blank=True, related_name='workout_level')
    image = models.ImageField(verbose_name=_('Превью'))
    description = models.TextField(verbose_name=_('Описание'))
    value = models.TextField(verbose_name=_('Польза'))
    sex = models.ManyToManyField(Sex, related_name='workout_sex', blank=True)
    troubles = models.ManyToManyField(Trouble, verbose_name=_('Проблемы'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Тренировка')
        verbose_name_plural = _('Тренировки')
        ordering = ['id']
