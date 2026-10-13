from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category


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