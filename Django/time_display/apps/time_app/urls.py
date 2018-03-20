from django.conf.urls import url
from . import views

urlpatterns = [
    #this is where i write my url
    url(r'^$',views.index ),
    url(r'^time_display$',views.index ),   
]