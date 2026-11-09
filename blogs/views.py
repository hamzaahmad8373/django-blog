
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category , Comment
from django.db.models import Q

def posts_by_category(request, category_id):
    # try:
    #     category= Category.objects.get(pk=category_id)
    # except:       
    #     return redirect('home')
    category = get_object_or_404(Category, pk=category_id)
    posts = Blog.objects.filter(
        status="published",
        category=category,
    ).order_by("-created_at")
    return render(
        request,
        "posts_by_category.html",
        {"category": category, "posts": posts}
    )

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='published')
    if request.method == 'POST':
         comment = Comment()
         comment.user = request.user
         comment.blog = single_blog
         comment.comment = request.POST['comment']
         comment.save()

         return HttpResponseRedirect(request.path_info )

    #COMMENTS
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()
    print('Comments=>', comments)
    context={
        'single_blog':single_blog,
        'comments':comments,
        'comment_count':comment_count
    }
    return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword)|Q(short_description__icontains=keyword)|Q(blog_body__icontains=keyword),status='published')
    context = {
        'blogs':blogs,
        'keyword':keyword,
    }
    return render(request, 'search.html',context)