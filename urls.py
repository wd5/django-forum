#from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url


#(?P<year>\d{4})
urlpatterns = patterns( 'forum',
    url( r'^forum-(?P<id>\d+)(?:\-(?P<slug>[\w\-]+))?/$', 'views.forum', name = 'forum-forum' ),
    url( r'^topic-(?P<id>\d+)(?:\-(?P<slug>[\w\-]+))?/$', 'views.topic', name = 'forum-topic' ),
#    url( r'^add-topic/$', 'views.add_topic', name = 'forum-add-topic' ),
#    url( r'^edit-topic/(?P<id>\d+)/$', 'views.edit_topic', name = 'forum-edit-topic' ),
    url( r'^add-post/(?P<forum>\d+)/$', 'views.add_post', name = 'forum-add-post' ),
    url( r'^edit-post/(?P<id>\d+)/$', 'views.edit_post', name = 'forum-edit-post' ),
    url( r'^$', 'views.home', name = 'forum-home' ),
 )

