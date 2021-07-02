from django.urls import include, path
from . import views


urlpatterns = [
    path('',views.reviews, name='reviews'), # url testimonial pages
    path('create/', views.leave_reviews, name='create_view'), # url object creation Review_new
    path('false/', views.leave_reviews_false, name='leave_reviews_false'),
]