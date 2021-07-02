from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.


class Question(models.Model): #Описание модели для сохранения вопросов
    email = models.CharField(max_length=30) #Почта
    name_person = models.CharField(max_length=30) #Имя
    theme_question = models.CharField(max_length=100) #Тема
    full_text = models.TextField(max_length=2000) #Основной текст
    created_time_quest = models.DateTimeField(default=timezone.now) #Время создания вопроса 
    def __str__(self): # Функция для вывода темы объекта при get()
        return self.theme_question

class Out_questiom(models.Model):
	email_answer = models.CharField(max_length=30)
	name_person_answer = models.CharField(max_length=30)
	theme_question_answer = models.CharField(max_length=100)
	full_text_answer = models.CharField(max_length=2000)
	full_text_answer_old = models.CharField(max_length=2000)
	created_time_quest_old = models.CharField(max_length=50)
	created_time_quest_answer= models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.theme_question_answer