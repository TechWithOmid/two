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
    content = RichTextField(blank=True, null=True)
    gategory = models.ManyToManyField(Category)
    date = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(Writer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title