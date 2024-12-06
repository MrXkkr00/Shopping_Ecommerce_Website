from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.




class Category(models.Model):
    name = models.CharField(_('Name'), max_length=120)
    # parent = models.
    image = models.ForeignKey('common.Media', on_delete=models.SET_NULL, null=True, blank=True )

    def __str__(self):
        return self.name




class Product(models.Model):
    name = models.CharField(_("Name"), max_length=120)
    price = models.FloatField(_('Price'))
    description = models.TextField(_('Description'))
    short_description = models.TextField(_('Short description'))
    quality = models.IntegerField(_('Quality'))
    instructions = models.TextField(_('Instructions'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    in_stock = models.BooleanField(_('In Stock'))
    brand = models.CharField(_('Brand'),max_length=120, )
    discount = models.IntegerField(_('Discount'))


    def __str__(self):
        return f"Name: {self.name}  |Price:  {self.price} | Quality: {self.quality} | brand: {self.brand}"



class ProductColor(models.Model):
    # image = models.ForeignKey
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_color')




class ProductSize(models.Model):
    value = models.CharField(_('Value'), max_length=120)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_size')




class ProductImage(models.Model):
    image= models.ForeignKey('common.Media', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')


class ProductReview(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='product_review')
    rank = models.IntegerField(_('Rank'))
    title = models.CharField(_('Title'), max_length=120)
    review = models.TextField(_('Review'))
    created_at = models.DateTimeField(_('Created at'))
    email = models.EmailField(_('Email'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_review')


    def __str__(self):
        return f"User : {self.user.name} | Product : {self.product.name} | Mavzu : {self.title}"


class Discount(models.Model):
    code = models.CharField(_('Code'), max_length=10)
    max_limit_price = models.CharField(_("Max Price"), max_length=12)
    percentage = models.IntegerField(_("Percentage"))



class WishList(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_wishlist')
