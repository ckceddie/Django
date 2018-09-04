from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^buy$', views.buy),     # This line has changed!
    url(r'^amadon$', views.amadon),     # This line has changed!
    url(r'^checkout$', views.checkout)     # This line has changed!
]
