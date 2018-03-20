from . import views
from django.conf.urls import url

urlpatterns = [
  url(r'^$', views.index),
  url(r'^register$', views.register),
  url(r'^login$', views.login),
  url(r'^quotes$',views.quotes, name = "quotes"),
  url(r'^add_quote$',views.add_quote, name = "add_quotes"),
  url(r'^add_favorites/(?P<id>\d+)$',views.add_favorites, name = "add_favorites"),
  url(r'^remove_favorites/(?P<id>\d+)$',views.remove_favorites, name = "remove_favorites"),
  url(r'^display_posts/(?P<id>\d+)$',views.display_posts, name = "display_posts"),
  url(r'^logout$', views.logout, name="logout"),
]


# urlpatterns = [
# 	url(r'^$', views.index),*********
# 	url(r'^register$', views.register),******
# 	url(r'^login$', views.login),******
#   url(r'^travel/destination$',views.travels),
# 	url(r'^logout$', views.logout, name="logout"),
# 	url(r'^travels/add$', views.addTrip, name="main"),
# 	url(r'^travels/destination/addTrip$', views.addTrip, name="add_trip"),
# 	url(r'^travels/destination/(?P<Trip_id>\d+)$', views.tripProfile),
# 	url(r'^travels/destination/(?P<Trip_id>\+)join$',views.join, name="join" )
# ]