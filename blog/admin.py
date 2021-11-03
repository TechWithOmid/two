from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post, Category, Writer


# Unregister Models
admin.site.unregister(Group)


# Register Models
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('title', 'category_list', 'publish_date', 'status', )
    list_filter = ('status', 'category__name', 'date',)
    list_editable = ('status', )
    search_fields = ['title']
    list_per_page = 5

    def category_list(self, obj):
        """ Show the category list in list_display """
        return "".join([f"{c.name} " for c in obj.category.all()])
    
    def publish_date(self,obj):
        """ Show the date in list_display using YY/MM/DD format """
        return obj.date.strftime("%Y/%m/%d")


@admin.register(Category)
class Category(admin.ModelAdmin):
    pass


@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    pass


# Other things
admin.site.site_header = 'مدیریت وبلاگ'
