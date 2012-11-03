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
# Create your models here.
#STATUS_CHOICES = (
#    ('active', 'active'),
#    ('inactive', 'inactive'),
#    ('draft', 'draft'),
#    ('deleted', 'deleted'),
#)
if 'south' in settings.INSTALLED_APPS:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules( [], ["^tinymce\.models.\HTMLField"] )

class Forum( MPTTModel ):
    parent = TreeForeignKey( 'self', null = True, blank = True, related_name = 'children' )
    title = models.CharField( max_length = 200, null = True, blank = True, default = '', )
    description = models.TextField(blank=True,help_text="Optional")
    forum_order = models.PositiveSmallIntegerField(blank=True, help_text="Optional", default=0)
    status = models.CharField( max_length = 15, choices = settings.STATUS_CHOICES, default = 'active', db_index = True )
    post_count = models.PositiveSmallIntegerField(blank=True, help_text="Optional", default=0)
    date_add = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    featured_until = models.DateTimeField()
    last_topic_edit = models.DateTimeField()
    last_topic_id = models.PositiveIntegerField()
    last_post_edit = models.DateTimeField()
    last_post_id = models.PositiveIntegerField()

    class MPTTMeta:
        order_insertion_by = ['title']

    def __unicode__( self ):
        return self.title

    def slug( self ):
        return slugify( self.title )

class Topic(models.Model):
    title = models.CharField( max_length = 200, null = True, blank = True, default = '', )
    forum = models.ForeignKey( Forum, null = True, blank = True, )


class Post( MPTTModel ):
    title = models.CharField( max_length = 200, null = True, blank = True, default = '', )
    content = tinymce_models.HTMLField()
    author = models.ForeignKey( User, related_name = "%(app_label)s_%(class)s_related" )
    parent = TreeForeignKey( 'self', null = True, blank = True, related_name = 'children' )
    forum = models.ForeignKey( Forum, null = True, blank = True, )
    topic = models.ForeignKey( Topic, null = True, blank = True, )
    date_add = models.DateTimeField( auto_now_add = True )
    date_edit = models.DateTimeField( auto_now = True )
    status = models.CharField( max_length = 15, choices = settings.STATUS_CHOICES, default = 'active', db_index = True )
    tags = TagField()


