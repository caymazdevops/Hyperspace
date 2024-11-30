from django.shortcuts import render
from core.models import BlogPost, SporPost

def dashboard(request):
    posts = BlogPost.objects.all()
    sports = SporPost.objects.all()

    context = {
        'posts': posts,
        'sports': sports,
    }

    return render(request, 'dashboard/index.html', context)


def sporpage(request):
    sports = SporPost.objects.all()

    return render(request, 'dashboard/sporpage.html', {'sports': sports})