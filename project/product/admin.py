from django.contrib import admin

from project.product.models import *
from project.order.models import *

# Register your models here.

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderProduct)