# Generated by Django 4.2.1 on 2024-09-17 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_filestask'),
    ]

    operations = [
        migrations.AddField(
            model_name='works',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, verbose_name='Слаг'),
        ),
    ]
