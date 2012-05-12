from django.contrib import admin
from quotes.models import Quote

class QuoteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Quote, QuoteAdmin)