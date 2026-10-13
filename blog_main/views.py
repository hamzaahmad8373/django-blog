from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Blog, Category

def home(request):
    feature_posts = Blog.objects.filter(is_featured=True ).order_by('-created_at')
    post = Blog.objects.filter(is_featured=False, status='published')
    context = {
        'feature_posts': feature_posts,
        'posts': post
    }
    return render(request, 'home.html', context)