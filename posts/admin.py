from django.contrib import admin
from .models import Post, Genre, Comment


class PostAdmin(admin.ModelAdmin):

    list_display = ('pk', 'text', 'pub_date', 'author', 'genre')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = "-пусто-"


admin.site.register(Post, PostAdmin)


class GenreAdmin(admin.ModelAdmin):

    list_display = ('pk', 'title', 'slug', 'description')
    search_fields = ('title',)
    list_filter = ('title',)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Genre, GenreAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'author', 'created')
    search_fields = ('text',)
    list_filter = ('created',)


admin.site.register(Comment, CommentAdmin)
