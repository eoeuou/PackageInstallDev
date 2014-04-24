from django.conf.urls import patterns, include, url
from blog.views import archive,get_now,get_books

urlpatterns = patterns('',
   url(r'^archive/$',archive),
   url(r'^books/$', get_books),
)