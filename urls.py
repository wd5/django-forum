#from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url


#(?P<year>\d{4})
urlpatterns = patterns('forum',
    url( r'^$', 'views.home', name = 'forum-home' )
)
#urlpatterns = patterns('zokiguide.forum',
#    (r'^$', 'views.welcome'),
#    (r'^category-(?P<id>\d+)/$', 'views.category',),
#    (r'^post-(?P<id>\d+)/$', 'views.post',),
##    (r'^ajax/upload_post_image/$', 'views.upload_post_image',),
#)
