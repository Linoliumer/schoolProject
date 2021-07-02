from django import forms
from .models import Question


class QuestionForm(forms.Form):
    email = forms.CharField(max_length=30)
    name_person = forms.CharField(max_length=30)
    theme_question = forms.CharField(max_length=100)
    full_text = forms.CharField(max_length=2000)
    def saved(self):
        new_question = Question(
            email = self.cleaned_data['email'],
            name_person = self.cleaned_data['name_person'],
            theme_question = self.cleaned_data['theme_question'],
            full_text = self.cleaned_data['full_text']
        )
        new_question.save()
        return new_question