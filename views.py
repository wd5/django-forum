from django.shortcuts import render, redirect
#from django.http import HttpResponse
#from django.db.models import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from . models import ForumForum, ForumPost
from common.utils import log

# Create your views here.

def get_forums( parent = 0 ):

    if int( parent ) == 0:
        return ForumForum.objects.filter( parent__isnull = True )

    return ForumForum.objects.filter( parent = parent )

def get_posts( forum ):
    posts = []
    return posts

def home( request ):

    forums = get_forums()

    data = {
        'forums':forums,
    }
    return render( request, 'forum/home.html', data )

def forum( request, id, slug ):

    id = int( id )


    try:
        forum = ForumForum.objects.get( pk = id )
    except ForumForum.DoesNotExist:
        raise Http404

    log( forum )


    if forum.slug() != slug:
        return redirect( 'forum-forum', id = id, slug = forum.slug(), permanent = True )

    forums = get_forums( forum.id )

    posts = ForumPost.objects.filter( forum = forum )

    data = {
        'forum':forum,
        'forums':forums,
        'posts':posts,
    }
    return render( request, 'forum/forums.html', data )

def topic( request ):
    data = {}
    return render( request, 'forum/topic.html', data )


#def add_forum( request ):
#    data = {}
#    return render( request, 'forum/topic.html', data )
#
#def edit_forum( request, id ):
#    data = {}
#    return render( request, 'forum/topic.html', data )

#def add_topic( request ):
#    data = {}
#    return render( request, 'forum/topic.html', data )
#
#def edit_topic( request, id ):
#    data = {}
#    return render( request, 'forum/topic.html', data )

def add_post( request, forum ):
    data = {}
    return render( request, 'forum/edit-post.html', data )

def edit_post( request, id ):
    data = {}
    return render( request, 'forum/edit-post.html', data )
