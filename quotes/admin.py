from django.contrib import admin
from quotes.models import Quote

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'quote', 'picture', 'is_active')
    list_editable = ('quote', 'picture', 'is_active')
    actions = ['mark_active', 'mark_inactive']

    def mark_active(self, request, queryset):
        queryset.update(is_active=True)

    def mark_inactive(self, request, queryset):
        queryset.update(is_active=False)

admin.site.register(Quote, QuoteAdmin)