from django import forms
from .models import Review_new

stop_list = {
    'бля',
    'хуй',
    'нахуй',
    'пизда',
    'ебать',
}

class Review_newForm(forms.Form):
    author_name = forms.CharField(max_length=30)
    rating = forms.CharField(max_length=1)
    text_quest = forms.CharField(max_length=500)
    def saved(self):
        new_review = Review_new(author_name = self.cleaned_data['author_name'],
            rating = self.cleaned_data['rating'],
            text_quest = self.cleaned_data['text_quest']
        )
        new_review.save()
        return new_review
    