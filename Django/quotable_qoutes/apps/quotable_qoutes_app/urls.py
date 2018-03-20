from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='user_name'),
    url(r'^validation$', views.validate, name="validate"),
    url(r'^quotes$', views.quotes, name='user_quotes'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^login$',views.login, name="loginInUser"),
]