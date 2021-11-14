from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post, Writer, Category



def home_page_view(request):
    """Home Page"""
    posts = Post.objects.filter(status='p').order_by('-date')
    paginator = Paginator(posts, 5)
    writer = Writer.objects.get(pk=1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'writer_info': writer,
    }
    return render(request, 'blog/index.html', context)


def detail_page_view(request, slug):
    """Detail Page"""
    obj = Post.objects.filter(status='p')
    post = get_object_or_404(obj, slug=slug)
    writer = Writer.objects.get(pk=1)
    context = {
        'post': post,
        'writer_info': writer,
    }
    return render(request, 'blog/blog-post.html', context)


def category_list_view(request):
    category_list = Category.objects.all()
    writer = Writer.objects.get(pk=1)

    context = {
        'categorys': category_list,
        'writer_info': writer,
    }
    return render(request, 'blog/category-list.html', context)


def category_post_view(request, category):
    posts = get_object_or_404(Category, slug=category).post_set.filter(status='p').order_by('-date')
    writer = Writer.objects.get(pk=1)

    context = {
        'posts': posts,
        'writer_info': writer,
    }
    return render(request, 'blog/category-post.html', context)


def search_result_view(request):
    """ serach for articles and return the results"""
    search_query = request.GET.get('query')
    posts = Post.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
    writer = Writer.objects.get(pk=1)

    context = {
        'posts': posts,
        'writer_info': writer,

    }
    return render(request, 'blog/search-result.html', context)


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
