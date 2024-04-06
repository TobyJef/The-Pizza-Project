from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

#summernote decorator for customer reviews
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

#filtered views for customer review posts
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
#summernote decorator for customer reviews

#summernote decorator for  business owner comment replies
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


