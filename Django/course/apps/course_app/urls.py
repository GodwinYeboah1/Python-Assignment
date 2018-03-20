from django.conf.urls import url
# link between client side and the server side
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^add$', views.add),
    url(r'^sending_out$',views.post_info),
]
