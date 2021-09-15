# Generated by Django 3.1.1 on 2021-04-26 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='День недели')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Уровень сложности')),
            ],
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1, verbose_name='Пол')),
            ],
        ),
        migrations.CreateModel(
            name='Trouble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Превью')),
            ],
            options={
                'verbose_name': 'Проблема',
                'verbose_name_plural': 'Проблемы',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('video', models.FileField(upload_to='', verbose_name='Видео')),
                ('duration', models.CharField(max_length=255, verbose_name='Длительность')),
                ('image', models.ImageField(upload_to='', verbose_name='Превью')),
                ('description', models.TextField(verbose_name='Описание')),
                ('value', models.TextField(verbose_name='Польза')),
                ('level', models.ManyToManyField(blank=True, related_name='workout_level', to='workout.Level')),
                ('periodicity', models.ManyToManyField(blank=True, related_name='workout_day', to='workout.Day')),
                ('sex', models.ManyToManyField(blank=True, related_name='workout_sex', to='workout.Sex')),
                ('troubles', models.ManyToManyField(to='workout.Trouble', verbose_name='Проблемы')),
            ],
            options={
                'verbose_name': 'Тренировка',
                'verbose_name_plural': 'Тренировки',
                'ordering': ['id'],
            },
        ),
    ]