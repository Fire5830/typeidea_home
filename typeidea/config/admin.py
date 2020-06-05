from django.contrib import admin
from .models import Links, SideBar
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin


@admin.register(Links, site=custom_site)
class LinksAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'create_time')
    fields = ('title', 'href', 'status', 'weight')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(LinksAdmin, self).save_model(request, obj, form, change)


@admin.register(SideBar, site=custom_site)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'content', 'display_type', 'create_time')
    fields = ('title', 'content', 'display_type')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(SideBarAdmin, self).save_model(request, obj, form, change)
