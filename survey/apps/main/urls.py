from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),   # This line has changed!
    url(r'^back$', views.back),   # This line has changed!
    url(r'^process$', views.process),     # This line has changed!
    url(r'^result$', views.result)     # This line has changed!
]
