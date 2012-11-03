from django.contrib import admin

from mptt.admin import MPTTModelAdmin
from . models import Forum, Topic, Post

class ForumAdmin( MPTTModelAdmin ):
    list_display = ( 'title', )
    search_fields = ( 'title', )

class TopicAdmin( admin.ModelAdmin ):
    list_display = ( 'title', )
    search_fields = ( 'title', )

class PostAdmin( MPTTModelAdmin ):
    list_display = ( 'title', )
    search_fields = ( 'title', )

admin.site.register( Forum, ForumAdmin )
admin.site.register( Topic, TopicAdmin )
admin.site.register( Post, PostAdmin )
