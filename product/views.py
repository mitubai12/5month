from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Review, Product, Category
from rest_framework.pagination import PageNumberPagination
from .serializers import ReviewSerializer, ProductSerializer, CategorySerializer, ReviewValidateSerializer, ProductValidateSerializer, CategoryValidateSerializer

class CustomPagination(PageNumberPagination):
    page_size = 5

class ReviewsListAPIView(ListCreateAPIView):
    queryset = Review.objects.select_related('product').all()
    serializer_class = ReviewSerializer
    pagination_class = CustomPagination

    def create(self, request, *args, **kwargs):
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ReviewsDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ProductsListAPIView(ListCreateAPIView):
    queryset = Product.objects.select_related('review').all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    def create(self, request, *args, **kwargs):
        serializer = ProductValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ProductsDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoriesListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPagination

    def create(self, request, *args, **kwargs):
        serializer = CategoryValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class CategoriesDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer