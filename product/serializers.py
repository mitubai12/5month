from rest_framework import serializers
from .models import Product, Review, Category
from django.db.models import Avg

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True, source='review_set')
    average_rating = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'category', 'reviews', 'average_rating']
    
    def get_average_rating(self, obj):
        average = obj.review_set.aggregate(Avg('stars'))['stars__avg']
        return round(average, 2) if average is not None else None

class ProductDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True, source='review_set')
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'category', 'reviews', 'average_rating', 'other_field1', 'other_field2']  # Add any additional fields if necessary
        depth = 1

    def get_average_rating(self, obj):
        average = obj.review_set.aggregate(Avg('stars'))['stars__avg']
        return round(average, 2) if average is not None else None

class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count']

    def get_products_count(self, obj):
        return Product.objects.filter(category=obj).count()
    class Meta:
        model = Category
        fields = '__all__'
        depth = 1