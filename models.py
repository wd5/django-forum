from django.db import models
from django.contrib.auth.models import User
from django.utils.html import strip_tags
from django.conf import settings

from mptt.models import MPTTModel, TreeForeignKey
from tinymce import models as tinymce_models
from slugify import slugify
from tagging.fields import TagField
from tagging.models import Tag
from urlparse import urlparse

if 'south' in settings.INSTALLED_APPS:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules( [], ["^tinymce\.models.\HTMLField"] )


class ForumForum( models.Model ):
    parent = models.ForeignKey( 'self', blank = True, null = True, default = 0 )
    title = models.CharField( 
        max_length = 200,
        null = True,
        blank = True,
        default = '',
    )
    content = models.TextField()
    date_add = models.DateTimeField( auto_now_add = True )
    is_featured = models.BooleanField( default = False )
    featured_until = models.DateTimeField( 
        blank = True,
        null = True,
    )
    status = models.CharField( 
        max_length = 15,
        choices = settings.STATUS_CHOICES,
        default = 'active',
        db_index = True
    )
    topic_count = models.PositiveSmallIntegerField( 
        default = 0,
        editable = False,
    )
    post_count = models.PositiveSmallIntegerField( 
        default = 0,
        editable = False,
    )
    last_topic_edit = models.DateTimeField( 
        blank = True,
        null = True,
        editable = False,
    )
    last_topic_id = models.PositiveIntegerField( 
        blank = True,
        null = True,
        editable = False,
    )
    last_post_edit = models.DateTimeField( 
        blank = True,
        null = True,
        editable = False,
    )
    last_post_id = models.PositiveIntegerField( 
        blank = True,
        null = True,
        editable = False,
    )

    def __unicode__( self ):
        return self.title

    def slug( self ):
        return slugify( self.title )



#class ForumTopic( models.Model ):
#    forum = models.ForeignKey( ForumForum )
#    author = models.ForeignKey( User, related_name = "%(app_label)s_%(class)s_related" )
#    title = models.CharField( max_length = 200, null = True, blank = True, default = '', )
#    content = tinymce_models.HTMLField()
#
#    def __unicode__( self ):
#        return self.title


class ForumPost( MPTTModel ):
    title = models.CharField( max_length = 200, null = True, blank = True, default = '', )
    content = tinymce_models.HTMLField()
    author = models.ForeignKey( User, related_name = "%(app_label)s_%(class)s_related" )
    parent = TreeForeignKey( 'self', related_name = 'children' )
    forum = models.ForeignKey( ForumForum )
#    topic = models.ForeignKey( ForumTopic )
    date_add = models.DateTimeField( auto_now_add = True )
    date_edit = models.DateTimeField( auto_now = True )
    status = models.CharField( 
        max_length = 15,
        choices = settings.STATUS_CHOICES,
        default = 'active',
        db_index = True
    )
    tags = TagField()

    class MPTTMeta:
        order_insertion_by = ['title']

    def __unicode__( self ):
        return self.title

    def slug( self ):
        return slugify( self.title )


