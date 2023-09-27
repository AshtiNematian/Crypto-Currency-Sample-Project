from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'published')
    list_filter = ("tags",)
    search_fields = ['title', 'tags']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
