from django.contrib import admin

from mptt.admin import MPTTModelAdmin
from . models import ForumForum, ForumPost

class ForumForumAdmin( admin.ModelAdmin ):
    list_display = ( 'title', )
    search_fields = ( 'title', )

#class ForumTopicAdmin( admin.ModelAdmin ):
#    list_display = ( 'title', )
#    search_fields = ( 'title', )

class ForumPostAdmin( MPTTModelAdmin ):
    list_display = ( 'title', )
    search_fields = ( 'title', )

admin.site.register( ForumForum, ForumForumAdmin )
#admin.site.register( ForumTopic, ForumTopicAdmin )
admin.site.register( ForumPost, ForumPostAdmin )
