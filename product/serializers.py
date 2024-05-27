from rest_framework import serializers
from .models import Product, Review, Category
from django.db.models import Avg
from rest_framework.exceptions import ValidationError

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, min_length=2, max_length=100)
    stars = serializers.IntegerField(min_value=1)
    product_id = serializers.IntegerField(min_value=1)

    def validate_product(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except:
            raise ValidationError('Director does not exist')
        return product_id

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


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, min_length=2, max_length=100)


class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True, source='review_set')
    average_rating = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'reviews', 'average_rating']
    
    def get_average_rating(self, obj):
        average = obj.review_set.aggregate(Avg('stars'))['stars__avg']
        return round(average, 2) if average is not None else None
    
class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, min_length=2, max_length=100)
    description = serializers.CharField(required=False)
    price = serializers.IntegerField(min_value=1500)

    def validate_category(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except:
            raise ValidationError('Director does not exist')
        return category_id

class ProductDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True, source='review_set')
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'category', 'reviews', 'average_rating']  # Add any additional fields if necessary
        depth = 1

    def get_average_rating(self, obj):
        average = obj.review_set.aggregate(Avg('stars'))['stars__avg']
        return round(average, 2) if average is not None else None
