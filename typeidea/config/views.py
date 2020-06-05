from django.views.generic import ListView

from blog.views import CommonViewMixin
from .models import Links


class LinkListView(CommonViewMixin, ListView):
    queryset = Links.objects.filter(status=Links.STATUS_NORMAL)
    template_name = 'config/links.html'
    context_object_name = 'link_list'


