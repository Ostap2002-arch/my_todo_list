from django.db import models
from django.urls import reverse


class Works(models.Model):
    title = models.CharField('Краткое название', max_length=255)
    description = models.TextField('Описание')
    PRIORITY =[
    (1, 'first'),
    (2, 'second'),
    (3, 'third'),
    (4, 'fourth')
    ]
    priority = models.IntegerField('Приоритетность', choices=PRIORITY)
    fileds = models.FileField('Дополнительный материал', upload_to='users/%Y/%m/%d')
    owner = models.ForeignKey('users.User' , verbose_name='Мои задачи', on_delete=models.CASCADE, default=None)
    categories = models.ForeignKey('Сategories' , verbose_name='Мои задачи', on_delete=models.CASCADE, default=None)
    date_tasks = models.DateTimeField('Дата события', null=True, blank=True)
    to_warn = models.DateTimeField('Предупредить за', null = True, blank=True)

class Сategories(models.Model):
    title = models.CharField('Категория', max_length=255)
    slug = models.SlugField('Slug', max_length=255, db_index=True, blank=True, default='')
    owner = models.ForeignKey('users.User' , verbose_name='Мои категории', on_delete=models.CASCADE, null=True, blank=True)
    push = models.BooleanField(verbose_name='Уведомления', null=True)
    color = models.ForeignKey('Color', verbose_name='ц  вет', on_delete=models.SET_NULL , default=None, null=True)
    date_creat = models.DateTimeField('Дата создания', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('create_and_show_tasks', kwargs={'slug_categories':self.slug})

class Color(models.Model):
    title = models.CharField('Название цвета', max_length=255)
    color = models.CharField('Цвет в hex', max_length=255)
    rgba = models.CharField('Цвет в rgba', max_length=255, default='0')



