from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from tinymce.models import HTMLField


class Category(models.Model):
    """
    Category only have name that posts will link to it
    """
    name = models.CharField(max_length=256)


class Writer(models.Model):
    """
    define who write the post(post owner)
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/')
    bio = models.TextField()
    # user be able to add Instagram, Twiiter, Yotube, Telegram link


class Post(models.Model):
    """
    blog articles 
    """
    title = models.CharField(max_length=256)
    thumbnail = models.ImageField(
        upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
    content = HTMLField()
    gategory = models.ManyToManyField(Category)
    date = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(Writer, on_delete=models.CASCADE)
