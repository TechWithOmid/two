from django.urls import path
from . import views


app_name='blog'
urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about-me/', views.about_me_view, name='about-me'),
    path('contact-me/', views.contact_me_view, name='contact-me'),
    path('categorys/', views.category_list_view, name='category-list'),
    path('categorys/<slug:category>', views.category_post_view, name='category-posts'),
    path('<slug:slug>/', views.detail_page_view, name='post_detail'),
]