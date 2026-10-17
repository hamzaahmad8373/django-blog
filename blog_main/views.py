from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Blog
from assignments.models import About

def home(request):
    feature_posts = Blog.objects.filter(is_featured=True ).order_by('-created_at')
    post = Blog.objects.filter(is_featured=False, status='published')

    try:
        about = About.objects.get()
    except:
        about = None
    
    context = {
        'feature_posts': feature_posts,
        'posts': post,
        'about': about
    }
    return render(request, 'home.html', context)