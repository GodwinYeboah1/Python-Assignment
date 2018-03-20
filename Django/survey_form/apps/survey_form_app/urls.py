# this page will take you to the view and matches that  method
from django.conf.urls import url  
from . import views
# from the root folder  import the views file


urlpatterns = [

# I am using the url function that i imported at the top
    url(r'^$',views.index),
    url(r'^result$',views.result),
    url(r'^process$',views.process),
]