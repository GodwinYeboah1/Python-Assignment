from django.conf.urls import url
from . import views
urlpatterns = [
    # dont forget the  patter godwin r'^ books$,
    url(r'^books$', views.books),
    url(r'^add_book$', views.add_book),
    url(r'^book_review$', views.book_reviews),
  
]