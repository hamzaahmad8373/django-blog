from django.urls import path
from . import views


urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    # category crud
    path('categories/',views.categories, name='categories'),
    path('categories/add/',views.add_category, name='add_category'),
    path('categories/edit/<int:pk>/',views.edit_category, name='edit_category'),
    path('categories/dlt/<int:pk>/',views.dlt_category, name='dlt_category'),
    # blog post crud
    path('posts/',views.posts, name='posts'),
    path('posts/add/',views.add_post, name='add_post'),
    path('posts/edit/<int:pk>/',views.edit_post, name='edit_post'),
    path('posts/dlt/<int:pk>/',views.dlt_post, name='dlt_post'),

]
