from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index, name='index'), # Output to the main page
    path('about_us/',views.about, name='about') # Output to page INFO
]