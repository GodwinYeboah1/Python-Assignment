from django.conf.urls import url
from . import views

# website url links bellow 

urlpatterns = [
    url(r'^$',views.index),
    url(r'^register$',views.register),
    url(r'^login$',views.login),

]
