from .models import Category
def get_cat(request):
    categories = Category.objects.all()
    return dict(categories=categories)