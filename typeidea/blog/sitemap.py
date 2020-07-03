from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Post


class PoseSitemap(Sitemap):
    changefreq = "always"
    prioity = 1.0
    protocol = 'https'

    def items(self):
        return Post.objects.filter(status=Post.STATUS_NORMAL)

    def lastmod(self, obj):
        return obj.created_time

    def location(self, obj):
        return reversed('post-detail', args=[obj.pk])

