from django.http import HttpResponse
from django.shortcuts import render,redirect
from blogs.models import Blog
from assignments.models import About
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

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

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html',context)
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html',context)


def logout(request):
    auth.logout(request)
    return redirect('home')