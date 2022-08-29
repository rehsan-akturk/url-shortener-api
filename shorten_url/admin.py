from django.contrib import admin

from shorten_url.models import ShortUrlModel


@admin.register(ShortUrlModel)
class ShortUrlAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_url', 'url', 'created_at', 'count')
    list_filter = ('created_at',)
