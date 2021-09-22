from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Category(models.Model):
    """
    Category only have name that posts will link to it
    """
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Writer(models.Model):
    """
    define who write the post(post owner)
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=128)
    avatar = models.ImageField(upload_to='avatar/')
    bio = models.TextField()
    # user be able to add Instagram, Twiiter, Yotube, Telegram link

    def __str__(self):
        return self.username


class Post(models.Model):
    """
    blog articles 
    """
    STATUS = {
        ('d', 'Draft'),
        ('p', 'Plublished'),
    }
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    thumbnail = models.ImageField(
        upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
    description = models.TextField(max_length=280)
    content = RichTextField()
    category = models.ManyToManyField(Category)
    date = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(Writer, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS, default='d')

    def __str__(self):
        return self.title