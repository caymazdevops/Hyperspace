from django.contrib import admin
from .models import BlogPost, Category, SporPost, EkonomiPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date')  # Blog yazısının başlığı, yazarı ve yayın tarihi görünsün
    search_fields = ('title', 'author', 'content')  # Arama için başlık, yazar ve içerik alanları
    list_filter = ('publish_date', 'categories')  # Filtreleme için yayın tarihi ve kategoriler

class SporPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date')  # Blog yazısının başlığı, yazarı ve yayın tarihi görünsün
    search_fields = ('title', 'author', 'content')  # Arama için başlık, yazar ve içerik alanları
    list_filter = ('publish_date', 'categories')  # Filtreleme için yayın tarihi ve kategoriler

class EkonomiPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date')  # Blog yazısının başlığı, yazarı ve yayın tarihi görünsün
    search_fields = ('title', 'author', 'content')  # Arama için başlık, yazar ve içerik alanları
    list_filter = ('publish_date', 'categories')  # Filtreleme için yayın tarihi ve kategoriler

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Kategori adını listele
    search_fields = ('name',)  # Kategori adında arama yapabilme

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SporPost, SporPostAdmin)
admin.site.register(EkonomiPost, EkonomiPostAdmin)



