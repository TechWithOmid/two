from django.urls import path
from django.urls import path
from . import views


app_name='blog'
urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('<slug:slug>/', views.detail_page_view, name='detail'),
]