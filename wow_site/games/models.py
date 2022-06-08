from django.db import models

class Games(models.Model):
    title = models.CharField(name="Название", max_length=30)
    info = models.TextField(name='Описание', blank=True)
    photo = models.ImageField(name='Фото', upload_to='photos/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
