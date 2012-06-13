from django.contrib import admin
from quotes.models import Quote

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('quote', 'author', 'picture_preview', 'is_active')
    actions = ['mark_active', 'mark_inactive']

    def mark_active(self, request, queryset):
        queryset.update(is_active=True)

    def mark_inactive(self, request, queryset):
        queryset.update(is_active=False)

    def picture_preview(self, obj):
        return """
         <a href="%(url)s" target="_blank"><img src="%(url)s" height="50" /></a>
         """ % { 'url' : obj.picture.url }
    picture_preview.allow_tags = True


admin.site.register(Quote, QuoteAdmin)