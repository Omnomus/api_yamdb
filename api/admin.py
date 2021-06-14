from django.contrib import admin

from .models import Comment, Review


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('review', 'text', 'author', 'pub_date',)
    search_fields = ('review', 'text', 'author', 'pub_date',)
    list_filter = ('pub_date'),
    empty_value_display = '-пусто-'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author', 'score', 'pub_date',)
    search_fields = ('title', 'text', 'author', 'score',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
