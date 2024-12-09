from django.contrib import admin
from orders.models import *
# Register your models here.


admin.site.register(Branch)
admin.site.register(Card)
admin.site.register(CartItem)
admin.site.register(DeliveryTarif)
admin.site.register(Discount)
admin.site.register(Order)