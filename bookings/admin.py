from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

#summernote decorator for customer reviews
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')
#summernote decorator for customer reviews



