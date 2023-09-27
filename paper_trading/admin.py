from django.contrib import admin
from paper_trading.models import PropertyPaperTrading, PaperTrading


class PropertyPaperTradingAdmin(admin.ModelAdmin):
    list_display = ('id','average_price', 'quantity', 'created_at')


class PaperTradingAdmin(admin.ModelAdmin):
    list_display = ('user','id')


admin.site.register(PaperTrading, PaperTradingAdmin)
admin.site.register(PropertyPaperTrading, PropertyPaperTradingAdmin)
