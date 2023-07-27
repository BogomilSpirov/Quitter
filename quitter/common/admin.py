from django.contrib import admin
from . import models


# Register your models here.


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
	list_display = ['id', 'user', 'for_quit']
	list_filter = ['user', 'for_quit']
	ordering = ['for_quit', 'user']


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ['id', 'user', 'for_quit', 'comment_text', 'published']
	list_filter = ['user', 'published']
	ordering = ['for_quit', 'user', 'published']


@admin.register(models.Follow)
class FollowAdmin(admin.ModelAdmin):
	list_display = ['id', 'user', 'for_user']
	list_filter = ['user', 'for_user']
	ordering = ['for_user', 'user']
