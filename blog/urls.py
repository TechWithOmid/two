from django.urls import path
from . import views


app_name='blog'
urlpatterns = [
    path('', views.home_page_view, name='home'),        # show the blog posts
    path('blog/', views.home_page_view, name='home'),   # show the blog posts
    path('about-me/', views.about_me_view, name='about-me'),
    path('contact-me/', views.contact_me_view, name='contact-me'),
    path('categorys/', views.category_list_view, name='category-list'),
    path('categorys/<slug:category>', views.category_post_view, name='category-posts'),
    path('search/', views.search_result_view, name='search-result'),
    path('blog/<slug:slug>/', views.detail_page_view, name='post_detail'),
]
