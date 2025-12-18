from django.contrib import admin

from .models import MediaItem, Screenshot


class ScreenshotInline(admin.TabularInline):
    model = Screenshot


class MediaItemAdmin(admin.ModelAdmin):
    inlines = [
        ScreenshotInline,
    ]


admin.site.register(MediaItem, MediaItemAdmin)
