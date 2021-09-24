from django.db import models
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post, Writer

def home_page_view(request):
    """Home Page"""
    posts = Post.objects.all().order_by('-date')
    writer_info = Writer.objects.get(pk=1)
    paginator = Paginator(posts, 5) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'writer_info': writer_info,
    }
    return render(request, 'blog/index.html', context)


def detail_page_view(request, slug):
    """Detail Page"""
    post = Post.objects.get(slug=slug)
    writer_info = Writer.objects.get(pk=1)
    context = {
        'post': post,
        'writer_info': writer_info,
    }
    return render(request, 'blog/blog-post.html', context)


def about_me_view(request):
    """about me page"""
    writer = Writer.objects.get(pk=1)
    context = {
        'writer_info': writer,
    }

    return render(request, 'blog/about-me.html', context)
