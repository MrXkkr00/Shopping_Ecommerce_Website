
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from rest_framework import serializers

from accounts.models import User, VerificationOtp
from accounts.utils import generate_code, send_email
from common.serializers import MediaSerializer
from core.settings import base
from products.models import Product, ProductReview, ProductSize, WishList, Category, ProductImage, ProductColor


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ("image",)




class ProductSerializer(serializers.ModelSerializer):
    thumbnail = MediaSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ("id", "name", "price", "category", "in_stock", "brand", "discount", "thumbnail")






class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = '__all__'

class ProductSizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductSize
        fields = ('value')


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ('user', 'rank', 'title', 'review', 'created_at', 'email', 'product')


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ('user', 'product')
