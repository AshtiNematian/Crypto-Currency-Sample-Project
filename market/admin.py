from django.contrib import admin
from market.models import Market, Assets, Portfolio, Comment, DisLike, Like


class AssetsAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


class MarketAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'id', 'body', 'active')


class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment')


class DislikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment')


admin.site.register(Assets, AssetsAdmin)
admin.site.register(Market, MarketAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(DisLike, DislikeAdmin)
admin.site.register(Like, LikeAdmin)
