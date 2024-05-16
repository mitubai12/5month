from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Review, Category
from .serializers import ProductSerializer, ProductDetailSerializer, ReviewDetailSerializer, ReviewSerializer, CategorySerializer, CategoryDetailSerializer


@api_view(['GET'])
def products_list_api_view(request):
    # step 1: Collect data from DB
    films = Product.objects.all()

    # step 2: List of films from DB convert to Dictionary
    list_ = ProductSerializer(films, many=True).data

    # step 3: Return list of dictionary as JSON
    return Response(data=list_, status=status.HTTP_200_OK)


@api_view(['GET'])
def products_detail_api_view(request, id): # 100
    try:
        film = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Film not found'})
    film_dict = ProductDetailSerializer(film).data
    return Response(data=film_dict)


@api_view(['GET'])
def categories_list_api_view(request):
    # step 1: Collect data from DB
    category = Category.objects.all()

    # step 2: List of films from DB convert to Dictionary
    list_ = CategorySerializer(category, many=True).data

    # step 3: Return list of dictionary as JSON
    return Response(data=list_, status=status.HTTP_200_OK)


@api_view(['GET'])
def categories_detail_api_view(request, id): # 100
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Film not found'})
    category_dict = CategoryDetailSerializer(category).data
    return Response(data=category_dict)


@api_view(['GET'])
def reviews_list_api_view(request):
    # step 1: Collect data from DB
    review = Review.objects.all()

    # step 2: List of films from DB convert to Dictionary
    list_ = ReviewSerializer(review, many=True).data

    # step 3: Return list of dictionary as JSON
    return Response(data=list_, status=status.HTTP_200_OK)


@api_view(['GET'])
def reviews_detail_api_view(request, id): # 100
    try:
        review = Review.objects.get(id=id)
    except review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Film not found'})
    review_dict = ReviewDetailSerializer(review).data
    return Response(data=review_dict)