from django.contrib import admin

from .models import Comment, Date

@admin.register(Date)
class DateAdmin(admin.ModelAdmin):
    list_items = ('id', 'date', 'name', 'is_read')
    list_display = list_items
    list_display_links = list_items
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_items = ('id', 'date', 'comment')
    list_display = list_items
    list_display_links = list_items