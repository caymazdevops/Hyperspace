from django.urls import path
from django.conf import settings
from . import views 
from .views import SporListCreateAPIView, BlogListCreateAPIView
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.category_list, name='category_list'),  # Ana sayfa
    path('contact', views.contact, name='contact'),
    #path('category', views.category, name='category'),
    path('allspor', views.spor_index, name='allspor'),
    path('allekonomi', views.ekonomi_index, name='allekonomi'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),  # Gönderi detay
    path('spor/<int:id>/', views.spor_detail, name='spor_detail'),  # Gönderi detay
    path('api/', SporListCreateAPIView.as_view(), name='blog-list-create'),
    path('apipost/', BlogListCreateAPIView.as_view(), name='blog-list-api'),
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)