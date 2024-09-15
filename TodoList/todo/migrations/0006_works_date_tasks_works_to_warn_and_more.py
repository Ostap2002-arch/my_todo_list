# Generated by Django 4.2.1 on 2024-09-15 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_сategories_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='works',
            name='date_tasks',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата события'),
        ),
        migrations.AddField(
            model_name='works',
            name='to_warn',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Предупредить за'),
        ),
        migrations.AlterField(
            model_name='сategories',
            name='color',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='todo.color', verbose_name='ц  вет'),
        ),
    ]