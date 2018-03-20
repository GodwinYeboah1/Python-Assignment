from django.conf.urls import url, include
from . import views

# the name of the url are here 
urlpatterns = [
    url(r'^$',views.home),
    url(r'^random_word/',views.generator_random),
    url(r'^reset/', views.reset),
]
