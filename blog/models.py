from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    """
    Category only have name that posts will link to it
    """
    name = models.CharField(max_length=256, verbose_name="دسته بندی")
    slug = models.SlugField(blank=True, null=True, unique=True, verbose_name="لینک")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category-posts', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Writer(models.Model):
    """
    define who write the post(post owner)
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    username = models.CharField(max_length=128, verbose_name="نام کاربری")
    avatar = models.ImageField(upload_to='avatar/', verbose_name="آواتار")
    bio = models.TextField(verbose_name="بیو") # show in menu bar
    about_me = RichTextField(null=True, blank=True, verbose_name="درباره من")  # show in about me page
    # user be able to add Instagram, Twitter, Youtube, Telegram link

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
    title = models.CharField(max_length=256, verbose_name="عنوان")
    slug = models.SlugField(verbose_name="لینک")
    thumbnail = models.ImageField(
        upload_to='uploads/%Y/%m/%d/', null=True, blank=True, verbose_name="عکس")
    description = models.TextField(max_length=280, verbose_name="توضیحات")
    content = RichTextField(verbose_name="محتوا")
    category = models.ManyToManyField(Category, verbose_name="دسته بندی")
    date = models.DateTimeField(default=timezone.now, verbose_name="تاریخ")
    owner = models.ForeignKey(Writer, on_delete=models.CASCADE, verbose_name="نویسنده")
    status = models.CharField(max_length=1, choices=STATUS, default='d', verbose_name="وضعیت")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])
