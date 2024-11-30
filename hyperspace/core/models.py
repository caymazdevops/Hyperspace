from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)  # Kategori adı

    def __str__(self):
        return self.name
    


class BlogPost(models.Model):
    title = models.CharField(max_length=200)  # Blog başlığı
    subtitle = models.CharField(max_length=300, blank=True, null=True)  # Blog alt başlığı (isteğe bağlı)
    author = models.CharField(max_length=100)  # Yazar adı
    content = models.TextField()  # Blog içeriği
    publish_date = models.DateTimeField(default=timezone.now)  # Yayın tarihi (otomatik doldurulacak)
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)  # Kapak resmi (isteğe bağlı)
    categories = models.ManyToManyField(Category, related_name='blog_posts', blank=True)  # Kategoriler
    
    def __str__(self):
        return self.title
    

class SporPost(models.Model):
    title = models.CharField(max_length=200)  # Blog başlığı
    subtitle = models.CharField(max_length=300, blank=True, null=True)  # Blog alt başlığı (isteğe bağlı)
    author = models.CharField(max_length=100)  # Yazar adı
    content = models.TextField()  # Blog içeriği
    publish_date = models.DateTimeField(default=timezone.now)  # Yayın tarihi (otomatik doldurulacak)
    featured_image = models.ImageField(upload_to='spor_images/', blank=True, null=True)  # Kapak resmi (isteğe bağlı)
    categories = models.ManyToManyField(Category, related_name='spor_posts', blank=True)  # Kategoriler
    
    def __str__(self):
        return self.title
    

class EkonomiPost(models.Model):
    title = models.CharField(max_length=200)  # Blog başlığı
    subtitle = models.CharField(max_length=300, blank=True, null=True)  # Blog alt başlığı (isteğe bağlı)
    author = models.CharField(max_length=100)  # Yazar adı
    content = models.TextField()  # Blog içeriği
    publish_date = models.DateTimeField(default=timezone.now)  # Yayın tarihi (otomatik doldurulacak)
    featured_image = models.ImageField(upload_to='ekonomi_images/', blank=True, null=True)  # Kapak resmi (isteğe bağlı)
    categories = models.ManyToManyField(Category, related_name='ekonomi_posts', blank=True)  # Kategoriler
    
    def __str__(self):
        return self.title
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"

