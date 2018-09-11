from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^users$', views.index),     # This line has changed!
    url(r'^users/new$', views.new),     # This line has changed!
    url(r'^users/add$', views.add),     # This line has changed!
    url(r'^users/update$', views.update),     # This line has changed!
    url(r'^users/(?P<id>\d+)$', views.show, name='my_show'),
    url(r'^users/(?P<id>\d+)/edit$', views.edit, name='my_edit'),
    url(r'^users/(?P<id>\d+)/delete$', views.delete, name='my_delete'),
]
