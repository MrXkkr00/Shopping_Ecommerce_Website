from django.contrib import admin
from django.contrib.auth.models import Group
from mptt.admin import MPTTModelAdmin

from products.models import *

# Register your models here.

class CustomMPTTModelAdmin(MPTTModelAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20
    mptt_indent_field = "name"

@admin.register(Category)
class CategoryAdmin(CustomMPTTModelAdmin):
    list_display = ["name", "parent"]


admin.site.register(Product)
admin.site.register(ProductColor)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
admin.site.register(ProductSize)

