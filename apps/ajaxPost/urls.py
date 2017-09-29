from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^create$', views.create),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^add_desc/(?P<id>\d+)$', views.add_desc),
    url(r'^edit_desc/(?P<id>\d+)$', views.edit_desc),
    url(r'^toggle_desc/(?P<id>\d+)$', views.toggle_desc),
]