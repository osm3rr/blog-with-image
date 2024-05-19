from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'author')
    list_filter = ("author",)
    search_fields = ['title', 'author']
    ordering = ('-created_at',)
    
admin.site.register(Post, PostAdmin)
