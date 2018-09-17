from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^login$', views.login),     # This line has changed!
    url(r'^books$', views.books),     # This line has changed!
    url(r'^books/(?P<book_id>[0-9]+)$', views.reviewList),     # This line has changed!
    url(r'^user/(?P<user_id>[0-9]+)$', views.user),     # This line has changed!
    url(r'^logout$', views.logout),     # This line has changed!
    url(r'^addBook$', views.addBook),     # This line has changed!
    url(r'^books/add_review$', views.add_review),     # This line has changed!
    url(r'^delete/(?P<review_id>[0-9]+)/(?P<book_id>[0-9]+)$', views.deleteReview),     # This line has changed!
    url(r'^add$', views.add),     # This line has changed!
    url(r'^register$', views.register)     # This line has changed!
]
