from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import truncatechars
from datetime import date


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

    class Meta:
        verbose_name = _("دسته بندی")
        verbose_name_plural = _("دسته بندی‌ها")
    

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

    class Meta:
        verbose_name = _("نویسنده")
        verbose_name_plural = _("نویسنده ها")


class Post(models.Model):
    """
    blog articles 
    """
    STATUS = {
        ('d', 'پیش‌نویس'),
        ('p', 'منتشر شده'),
    }
    title = models.CharField(max_length=256, verbose_name="عنوان")
    slug = models.SlugField(verbose_name="لینک")
    thumbnail = models.ImageField(
        upload_to='uploads/%Y/%m/%d/', null=True, blank=True, verbose_name="عکس")
    content = RichTextField(verbose_name="محتوا")
    category = models.ManyToManyField(Category, verbose_name="دسته بندی")
    keywords=models.CharField(max_length=1024, verbose_name="کلمات کلیدی", default="وبلاگ امید,")
    pub_date = models.DateTimeField(default=timezone.now, verbose_name="تاریخ")
    owner = models.ForeignKey(Writer, on_delete=models.CASCADE, verbose_name="نویسنده")
    status = models.CharField(max_length=1, choices=STATUS, default='d', verbose_name="وضعیت")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Return absolute url of post"""
        return reverse('blog:post_detail', args=[self.slug])

    @property
    def description(self):
        """Short description of post"""
        return truncatechars(self.content, 100)

    @property
    def passed_time_since_publish(self):
        """Calculate the passed days, weeks, months, years since article published"""
        today = date.today()
        passed_days = str(today - self.pub_date.date()).split(',', 1)[0].split(' ', 1)[0]
        
        if self.pub_date.date() == date.today():
            return "امروز"
        elif self.pub_date.date() < date.today():
            if int(passed_days) < 7:
                return f"{passed_days} روز قبل"
            if int(passed_days) < 30:
                passed_weeks = round(int(passed_days) / 7)
                return f"{passed_weeks} هفته قبل"
            elif int(passed_days) < 355 and int(passed_days) > 30:
                passed_months = round(int(passed_days) / 30)
                return f"{passed_months} ماه قبل"
            elif int(passed_days) > 355:
                passed_years = round(int(passed_days) / 355)
                return f"{passed_years} سال قبل"

    class Meta:
        verbose_name = _("پست")
        verbose_name_plural = _("پست ها")

