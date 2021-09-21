from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Writer

def home_page_view(request):
    """Home Page"""
    posts = Post.objects.all()
    writer_info = Writer.objects.get(pk=1)
    context = {
        'posts': posts,
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