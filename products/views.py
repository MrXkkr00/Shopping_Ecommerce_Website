from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Category, Product, ProductColor, WishList, ProductReview, ProductImage, ProductSize
from products.serializers import CategorySerializer, ProductSerializer, ProductColorSerializer, WishListSerializer, \
    ProductReviewSerializer, ProductImageSerializer, ProductSizeSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class CategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None


class ProductAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['category', "colour", "size"]

    # def get_queryset(self):
    #     min_price = self.request.query_params.get("min_price")
    #     max_price = self.request.query_params.get("max_price")
    #     if min_price and max_price:
    #         queryset = self.queryset.filter(price__gte=min_price, price__lte=max_price)
    #     elif min_price is None and max_price:
    #         queryset = self.queryset.filter(price__lte=max_price)
    #
    #     elif max_price is None and min_price:
    #         queryset = self.queryset.filter(price__gte=min_price)
    #     else:
    #         queryset = self.queryset.all()
    #     return queryset

class ProductColorAPIView(ListAPIView):
    queryset = ProductColor.objects.all()
    serializer_class = ProductColorSerializer


class ProductSizeAPIView(APIView):
    queryset = ProductSize.objects.all()
    serializer_class = ProductSizeSerializer


class ProductImageAPIView(APIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class ProductReviewAPIView(APIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer


class WishListAPIView(APIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer