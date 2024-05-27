from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Review, Category
from .serializers import ProductSerializer, ProductDetailSerializer, ReviewSerializer, CategorySerializer, ProductValidateSerializer, ReviewValidateSerializer, CategoryValidateSerializer

@api_view(['GET', 'POST'])
def reviews_list_api_view(request):
    if request.method == "GET":
        # Collect data from DB
        reviews = Review.objects.select_related('product').all()
        # Convert list of reviews to Dictionary
        data = ReviewSerializer(reviews, many=True).data
        # Return list of dictionary as JSON
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': serializer.errors})
        text = serializer.validated_data.get('text'),
        stars = serializer.validated_data.get('stars')
        product_id = serializer.validated_data.get('product_id')

        review = Review.objects.create(
           text=text,
           stars=stars,
           product_id=product_id
        )
        review.save()
        print('s')

        return Response(status=status.HTTP_201_CREATED,
                        data=ReviewSerializer(review).data)

@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail_api_view(request, id): 
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Review not found'})
    try:
        review = Category.objects.get(id=id)
    except review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'review not found'})
    if request.method == 'GET':
        data = ReviewSerializer(review).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        review.text = serializer.validated_data.get('text'),
        review.stars = serializer.validated_data.get('stars')
        review.product_id = serializer.validated_data.get('product_id')
        review.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=ReviewSerializer(review).data)
    elif request.method == 'DELETE':
        try:
            review.delete()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'error': 'review protected'})
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def products_list_api_view(request):
    if request.method == 'GET':
        products = Product.objects.select_related('review').all()
        data = ProductSerializer(products, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ProductValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': serializer.errors})

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        price = serializer.validated_data.get('price')

        product = Product.objects.create(
            title=title,
            description=description,
            price=price,
        )
        product.save()

        return Response(status=status.HTTP_201_CREATED,
                        data=ProductSerializer(product).data)

@api_view(['GET', 'PUT', 'DELETE'])
def products_detail_api_view(request, id): 
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Product not found'})
    if request.method == 'GET':
        data = ProductDetailSerializer(product).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = ProductValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product.title = serializer.validated_data.get('title')
        product.description = serializer.validated_data.get('description')

        product.price = serializer.validated_data.get('price')
        product.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=ProductDetailSerializer(product).data)
    elif request.method == 'DELETE':
        try:
            product.delete()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'error': 'product protected'})
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def categories_list_api_view(request):
    if request.method == 'GET':
        # Collect data from DB
        categories = Category.objects.all()
        # Convert list of categories to Dictionary
        data = CategorySerializer(categories, many=True).data
        # Return list of dictionary as JSON
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CategoryValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': serializer.errors})
        
        name = serializer.validated_data.get('name')

        category = Category.objects.create(
            name=name
        )
        category.save()
        print('s')

        return Response(status=status.HTTP_201_CREATED,
                        data=CategorySerializer(category).data)


@api_view(['GET', 'PUT', 'DELETE'])
def categories_detail_api_view(request, id): 
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Category not found'})
    if request.method == 'GET':
        data = CategorySerializer(category).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = CategoryValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        category.name = serializer.validated_data.get('name')
        category.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=CategorySerializer(category).data)
    elif request.method == 'DELETE':
        try:
            category.delete()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'error': 'category protected'})
        return Response(status=status.HTTP_204_NO_CONTENT)

