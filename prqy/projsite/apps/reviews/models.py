from django.conf import settings
from django.db import models
from django.utils import timezone


class Review_new(models.Model): #NEW #модель отзыва
    author_name = models.CharField(max_length=30) #Автор
    rating = models.CharField(max_length=1) #Рейтинг
    text_quest = models.TextField(max_length=500) #Текст отзыва
    date_time_create = models.DateTimeField(default=timezone.now) #Время создания объекта
    def __str__(self): # Функция для вывода текста объекта при get()
        return self.text_quest
