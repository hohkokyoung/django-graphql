from django.db import models
from django.contrib.auth import get_user_model

from project.product.models import Product

User = get_user_model()

# Create your models here.
class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, models.CASCADE)

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()