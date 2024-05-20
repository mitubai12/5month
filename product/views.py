from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Review, Category
from .serializers import ProductSerializer, ProductDetailSerializer, ReviewSerializer, CategorySerializer

@api_view(['GET'])
def products_list_api_view(request):
    # Collect data from DB
    products = Product.objects.select_related('category').all()
    # Convert list of products to Dictionary
    data = ProductSerializer(products, many=True).data
    # Return list of dictionary as JSON
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def products_detail_api_view(request, id): 
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Product not found'})
    data = ProductDetailSerializer(product).data
    return Response(data=data)

@api_view(['GET'])
def categories_list_api_view(request):
    # Collect data from DB
    categories = Category.objects.all()
    # Convert list of categories to Dictionary
    data = CategorySerializer(categories, many=True).data
    # Return list of dictionary as JSON
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def categories_detail_api_view(request, id): 
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Category not found'})
    data = CategorySerializer(category).data
    return Response(data=data)

@api_view(['GET'])
def reviews_list_api_view(request):
    # Collect data from DB
    reviews = Review.objects.select_related('product').all()
    # Convert list of reviews to Dictionary
    data = ReviewSerializer(reviews, many=True).data
    # Return list of dictionary as JSON
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def reviews_detail_api_view(request, id): 
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Review not found'})
    data = ReviewSerializer(review).data
    return Response(data=data)