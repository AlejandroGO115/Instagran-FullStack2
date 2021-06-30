from django.contrib import admin
from .models import Post, BlogComment

class ComentarioEnLinea(admin.StackedInline):
    model = BlogComment

#Para poder agregar los comentarios dentro del Post
class PostAdmin(admin.ModelAdmin):
    inlines = [
        ComentarioEnLinea,
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(BlogComment)