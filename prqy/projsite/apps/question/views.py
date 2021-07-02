from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render 
from .models import Question
from .forms import QuestionForm

def question(request):
    return render(request,'question/questionsPage.html')

def custom_404(request, exception):
    return render(request, 'question/404.html', {}, status=404)


def create_question(request): # Функция создания и сохранения объекта Review_new
    if request.method == "POST": # Объявление искомого метода
        list_quest={
            'email': request.POST.get("email"),
            'name_person': request.POST.get("name_person"),
            'theme_question': request.POST.get("theme_question"),
            'full_text': request.POST.get("full_text"),
        }
        question_form = QuestionForm(list_quest)
        if question_form.is_valid():
            question_form.saved()
            return HttpResponseRedirect("/question/")
        else:
            return render(request,'errorsPage.html')
    else:
        return HttpResponseRedirect("/reviews/false")