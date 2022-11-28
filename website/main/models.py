from django.db import models


# Create your models here.

class Book(models.Model):
    author = models.CharField('Автор', max_length=50)
    name = models.CharField('Название', max_length=100)
    price = models.FloatField('Цена')
    description = models.TextField('Описание')

    def __str__(self):
        return self.name
