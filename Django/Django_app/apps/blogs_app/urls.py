from django.conf.urls import url, include
from . import views

urlpatterns = [

    # this is how you create your route
   url(r'^$', views.index),
   url(r'^new/$',views.new),
   url(r'^create/$',views.create),
#    make sure to look over this bellow 
   url(r'^(?P<number>\d+)/$',views.show),
#  (this is how you are able to use a varabile from the view.py)
   url(r'^(?P<number>\d+)/edit/$',views.edit),
   url(r'^(?P<number>\d+)/delete/$',views.destroy)
]
