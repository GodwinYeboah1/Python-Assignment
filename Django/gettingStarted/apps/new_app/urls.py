from django.conf.urls import url
from . import views
urlpatterns =[
    url(r'^$', views.index) ,
    url(r'^create$', views.create),
    url(r'show$',views.show),
    url(r'update$',views.update),
]

# regex 
 # url(r'^(?P\d+)$', views.show),
    # url(r'^(?P\w+)$', views.show_word),
    # url(r'^/2003/$', views.special_case_2003),
    # url(r'^(?P[0-9]{4})$', views.year_archive),
    # url(r'^(?P[0-9]{4})/(?P[0-9]{2}$', views.month_archive),