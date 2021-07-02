from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Review_new
from .forms import Review_newForm




def leave_reviews_false(request):
    return render(request,'errorsPage.html')

def reviews(request):
    # Passing a list of 12 objects (by filter) Review_new in html
    reviews_list = Review_new.objects.order_by('-date_time_create')[:20]
    return render(request,'reviews/reviewsPage.html', {'reviews_list':reviews_list})


def leave_reviews(request): # Object creation and saving function Review_new
    if request.method == "POST": # Declaring the required method
        list_post={
            'author_name': request.POST.get("name"),
            'rating': request.POST.get("rating"),
            'text_quest': request.POST.get("text"),
        }
        review_form = Review_newForm(list_post)
        if review_form.is_valid(): #and review_form.clean_text():
            review_form.saved()
            return HttpResponseRedirect("/reviews/")
        else:
            return HttpResponseRedirect("/reviews/false")
    else:
        return HttpResponseRedirect("/reviews/false")

