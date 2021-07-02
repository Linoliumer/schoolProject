from django.shortcuts import render
from reviews.models import Review_new


def error_404_view(request, exception): # Error handling template output
    return render(request, 'errorsPage.html')

def index(request): # Displaying the master page template
	# Passing a list with 3 objects (by date) from the model Review_new
    reviews_list_main = Review_new.objects.order_by('-date_time_create')[:3] 
    return render(request,'info_page/homePage.html', {'reviews_list_main':reviews_list_main})

  
def about(request): # Output of the INFO page template
    return render(request,'info_page/aboutPage.html')