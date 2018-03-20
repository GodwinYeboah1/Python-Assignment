from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^quotes$',views.quotes),
    url(r'^check_quote$',views.check_quote)



]