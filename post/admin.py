from django.contrib import admin

from post.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status', 'tags')
    prepopulated_fields = {'slug': ('title',)}