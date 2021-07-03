from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=256)


class Post(models.Model):
    title = models.CharField(max_length=256)
    thumbnail = models.ImageField(
        upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
    content = models.TextField()
    gategory = models.ManyToManyField(Category)
    date = models.DateTimeField(default=timezone.now)
