from django.contrib import admin
from django.contrib.auth.models import Group

from products.models import *

# Register your models here.

admin.site.register(Categories)
admin.site.register(ProductColor)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
admin.site.register(ProductSize)

