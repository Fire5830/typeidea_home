"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

import xadmin
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

# from blog.views import post_list
# from blog.views import  post_detail
from blog.views import IndexView, CategoryView, TagView, PostDetailView, SearchView, AuthorView
from blog.apis import PostViewSet, CategoryViewSet
from config.views import LinkListView
from comment.views import CommentView
from typeidea.custom_site import custom_site
from .autocomplete import CategoryAutocomplete, TagsAutocomplete
# from blog.apis import post_list, PostList


router = DefaultRouter()
router.register(r'post', PostViewSet, basename='api-post')
router.register(r'category', CategoryViewSet, basename='api-category')
app_name = 'blog'

urlpatterns = [
    # path('', post_list, name='index'),
    path('', IndexView.as_view(), name='index'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='category-list'),
    path('tag/<int:tag_id>/', TagView.as_view(), name='tag-list'),
    # path('post/<int:post_id>.html', post_detail, name='post-detail'),
    path('post/<int:post_id>.html', PostDetailView.as_view(), name='post-detail'),
    path('search/', SearchView.as_view(), name='search'),
    path('author/<int:owner_id>/', AuthorView.as_view(), name='author'),
    path('links/', LinkListView.as_view(), name='links'),
    path('comment/', CommentView.as_view(), name='comment'),
    path('super_admin/', admin.site.urls, name='super-admin'),
    path('admin/', custom_site.urls, name='admin'),
    path('xadmin/', xadmin.site.urls, name='admin'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('category-autocomplete/', CategoryAutocomplete.as_view(), name='category-autocomplete'),
    path('tag-autocomplete/', TagsAutocomplete.as_view(), name='tag-autocomplete'),
    # path('api/post/', post_list, name='post-list'),
    # path('api/post/', PostList.as_view(), name='post-list'),
    path('api/', include((router.urls, 'blog'), namespace="api")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 配置ebug_toolbar
# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#
#     ] + urlpatterns


# 配置silk
if settings.DEBUG:
    urlpatterns += [url(r'^silk/', include('silk.urls', namespace='silk'))]
