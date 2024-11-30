from rest_framework import serializers
from .models import SporPost, Category, BlogPost  # Modellerinizi içe aktarın


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']  # Category modelinde hangi alanlar varsa buraya ekleyin

class BlogPostSerializer(serializers.ModelSerializer):
    # Many-to-Many olan `categories` için ilişkiyi göstermek adına bir nested serializer kullanıyoruz.
    categories = CategorySerializer(many=True, read_only=True)
    featured_image = serializers.ImageField(required=False)  # Resim alanını işlemek için

    class Meta:
        model = SporPost
        fields = [
            'id',
            'title',
            'subtitle',
            'author',
            'content',
            'publish_date',
            'featured_image',
            'categories'
        ]

class SporPostSerializer(serializers.ModelSerializer):
    # Many-to-Many olan `categories` için ilişkiyi göstermek adına bir nested serializer kullanıyoruz.
    categories = CategorySerializer(many=True, read_only=True)
    featured_image = serializers.ImageField(required=False)  # Resim alanını işlemek için

    class Meta:
        model = SporPost
        fields = [
            'id',
            'title',
            'subtitle',
            'author',
            'content',
            'publish_date',
            'featured_image',
            'categories'
        ]