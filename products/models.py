from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey

from common.models import Media
from products.managers import ProductManager
from django.core.cache import cache


# Create your models here.




class Category(MPTTModel):
    name = models.CharField(_("name"), max_length=255)
    image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    # lft  = models.CharField(max_length=255)
    # rght  = models.CharField(max_length=255)
    # tree_id  = models.IntegerField()
    # level  = models.CharField(max_length=255)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")  # Bo'limlar
        verbose_name_plural = _("Categories")

    class MPTTMeta:
        order_insertion_by = ['name']






class Product(models.Model):
    name = models.CharField(_("Name"), max_length=120)
    price = models.FloatField(_('Price'))
    description = models.TextField(_('Description'))
    short_description = models.TextField(_('Short description'))
    quality = models.IntegerField(_('Quality'))
    instructions = models.TextField(_('Instructions'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    in_stock = models.BooleanField(_('In Stock'), default=True)
    brand = models.CharField(_('Brand'),max_length=120, )
    discount = models.IntegerField(_('Discount'), help_text=_("in percentage"))
    thumbnail = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)

    objects = ProductManager()



    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     cache.delete("all_products")
    #     self.category.save()





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






class WishList(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_wishlist')
