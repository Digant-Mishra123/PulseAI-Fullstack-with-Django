from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin

from blog.models import BlogCategory
from blog.models import Blog,Comment
# Register your models here.

# class BlogAdmin(admin.ModelAdmin):
class BlogAdmin(SummernoteModelAdmin):
    list_display = ('title','category','created_at','publish')
    search_fields = ('title','content')
    list_filter = ('category', 'publish')
    list_editable = ('publish', )
    # list_per_page = 1
    summernote_fields = ('content',)
admin.site.register(BlogCategory)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment)
