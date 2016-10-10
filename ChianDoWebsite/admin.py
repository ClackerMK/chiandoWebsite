from django.contrib import admin
from .models import *

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ('name', 'text', "pinned")}),
        ("Advanced", {'fields': ('pub_date','visible','thumbnail',), "classes": ('collapse',)}),
    ]

class GalleryAdmin(admin.ModelAdmin):
    fields = ('blog',)

class EventAdmin(admin.ModelAdmin):
    fields =  ('start_date','end_date','start_time','end_time','place','gps_lon','gps_lat','blog')

class GalleryPictureInline(admin.StackedInline):
    model = GalleryPicture
    extra = 1

class PictureAdmin(admin.ModelAdmin):
    fields = ('path',)
    inlines = [GalleryPictureInline]

admin.site.register(Blog, BlogAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Picture, PictureAdmin)
