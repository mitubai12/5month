from django.contrib import admin
from django.urls import path, include
from product.views import (
    ProductsListAPIView,
    ProductsDetailAPIView,
    CategoriesListAPIView,
    CategoriesDetailAPIView,
    ReviewsListAPIView,
    ReviewsDetailAPIView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls')),

    path('api/v1/products/', ProductsListAPIView.as_view(), name='products-list'),
    path('api/v1/products/<int:pk>/', ProductsDetailAPIView.as_view(), name='products-detail'),

    path('api/v1/categories/', CategoriesListAPIView.as_view(), name='categories-list'),
    path('api/v1/categories/<int:pk>/', CategoriesDetailAPIView.as_view(), name='categories-detail'),

    path('api/v1/reviews/', ReviewsListAPIView.as_view(), name='reviews-list'),
    path('api/v1/reviews/<int:pk>/', ReviewsDetailAPIView.as_view(), name='reviews-detail'),
]
