from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
        "posts": PostSitemap,
        }

urlpatterns = [
    path('dj-admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap'),
    url(r'^comments/', include('django_comments_xtd.urls')),
]


# serve the static file in debug mode
if settings.DEBUG=="True":
    urlpatterns += static(settings.MEDIA_URL,
                                document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                                document_root=settings.STATIC_ROOT)

