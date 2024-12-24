from django.urls import path

from products.views import CategoryAPIView, ProductAPIView, ProductColorAPIView, ProductSizeAPIView, ProductImageAPIView, \
    ProductReviewAPIView, WishListAPIView

urlpatterns = [
    path('categories/', CategoryAPIView.as_view(), name='categories'),
    path('products/', ProductAPIView.as_view(), name='products'),
    path('product-colors/', ProductColorAPIView.as_view(), name='product_colors'),
    path('product-sizes/', ProductSizeAPIView.as_view(), name='product_sizes'),
    path('product-images/', ProductImageAPIView.as_view(), name='product_images'),
    path('product-reviews/', ProductReviewAPIView.as_view(), name='product_reviews'),
    path('wishlists/', WishListAPIView.as_view(), name='wishlists')
]