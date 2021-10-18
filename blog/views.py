from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post, Writer, Category


def home_page_view(request):
    """Home Page"""
    posts = Post.objects.all().order_by('-date')
    paginator = Paginator(posts, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog/index.html', context)


def detail_page_view(request, slug):
    """Detail Page"""
    post = Post.objects.get(slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'blog/blog-post.html', context)


def category_list_view(request):
    category_list = Category.objects.all()

    context = {
        'categorys': category_list,
    }
    return render(request, 'blog/category-list.html', context)


def category_post_view(request, category):
    posts = Category.objects.get(slug=category).post_set.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/category-post.html', context)


def about_me_view(request):
    """about me page"""
    writer = Writer.objects.get(pk=1)
    context = {
        'writer_info': writer,
    }

    return render(request, 'blog/about-me.html', context)


def contact_me_view(request):
    """contact page"""
    writer = Writer.objects.get(pk=1)
    context = {
        'writer_info': writer,
    }

    return render(request, 'blog/contact-me.html', context)
