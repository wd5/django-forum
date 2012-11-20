from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home( request ):
    data = {}
    return render( request, 'forum/home.html', data )

def forum(request):
    data = {}
    return render( request, 'forum/forums.html', data )

def topic( request ):
    data = {}
    return render( request, 'forum/topic.html', data )
