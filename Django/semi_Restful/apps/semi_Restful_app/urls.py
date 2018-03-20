from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^user/',views.index ,name='all_user'),
    url(r'^new$',views.new, name ="new_user"),
# this route bellow takes the post form data to the create methods
    url(r'^create$',views.create, name ="create_user"),
# this is how you show varibale (?P <>)in the url
    url(r'^show/(?P<id>\d+)$',views.show, name ="show_user"),
    url(r'^destroy/(?P<id>\d+)$', views.delete, name = "delete_user"),


]
