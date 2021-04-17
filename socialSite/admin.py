from django.contrib import admin
from .models import User, Post, Page, Song
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'date_join']


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['page_title', 'page_creations', 'user']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display= ['post_title', 'post_pub_date', 'page']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song_title', 'duration', 'written_by']
