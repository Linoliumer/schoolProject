from django.urls import include, path
from . import views



urlpatterns = [
    path('', views.question, name='question'), # url самой страницы
    path('create_quest/', views.create_question, name='create_quest') # url для создания новой модели через формы в html шаблоне
]

