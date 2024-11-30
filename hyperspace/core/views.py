from django.shortcuts import render
from django.core.paginator import Paginator
from rest_framework.generics import ListAPIView
from rest_framework import generics
from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Category, SporPost, EkonomiPost
from .serializers import SporPostSerializer, BlogPostSerializer,CategorySerializer


class SporListCreateAPIView(generics.ListCreateAPIView):
    queryset = SporPost.objects.all()
    serializer_class = SporPostSerializer


class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        limit = self.request.query_params.get('limit')  # URL'den 'limit' parametresini al
        if limit:
            return super().get_queryset()[:int(limit)]
        return super().get_queryset()

def category_list(request):
    categories = Category.objects.all()  # Tüm kategorileri çek
    return render(request, 'category_list.html', {'categories': categories})

def index(request):
    categories = Category.objects.all()[:4]
    posts = BlogPost.objects.all()[:10]
    sports= SporPost.objects.all()[:4]
    ekonomi= EkonomiPost.objects.all()[:4]
  

    # Her kategoriye ait blog yazılarını al
    category_blog_posts = {}
    for category in categories:
        category_blog_posts[category] = BlogPost.objects.filter(categories=category)  

    context = {
        'category_blog_posts': category_blog_posts,
        'posts': posts,
        'sports': sports,
        'ekonomi': ekonomi,
    }
    return render(request, 'core/index.html', context)

def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    blog_posts = category.blog_posts.all()  # BlogPost ilişkili içerikleri al
    spor_posts = category.spor_posts.all()  # SporPost ilişkili içerikleri al
    ekonomi_posts = category.ekonomi_posts.all()  # EkonomiPost ilişkili içerikleri al

    return render(request, 'core/category_posts.html', {
        'category': category,
        'blog_posts': blog_posts,
        'spor_posts': spor_posts,
        'ekonomi_posts': ekonomi_posts,
    })



def post_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'core/post_detail.html', {'post': post})

def spor_index(request):
    categories = Category.objects.all()
    sport = SporPost.objects.all()

    category_blog_posts = {}
    for category in categories:
        category_blog_posts[category] = SporPost.objects.filter(categories=category) 

    context = {
        'category_blog_posts': category_blog_posts,
        'sport': sport
        
    }

    return render(request, 'core/spor.html', context)


def ekonomi_index(request):
    categories = Category.objects.all()
    ekonomi = EkonomiPost.objects.all()

    category_blog_posts = {}
    for category in categories:
        category_blog_posts[category] = SporPost.objects.filter(categories=category) 

    context = {
        'category_blog_posts': category_blog_posts,
        'ekonomi': ekonomi
        
    }

    return render(request, 'core/ekonomi.html', context)


def spor_detail(request, id):
    sport = get_object_or_404(SporPost, id=id)
    return render(request, 'core/spor_detail.html', {'sport': sport})

def about(request):
    return render(request, 'core/about.html')


def posts_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = BlogPost.objects.filter(category=category)

    
    
    return render(request, 'posts_by_category.html', {'category': category, 'posts': posts})

def contact(request):
    return render(request, 'core/contact.html')

