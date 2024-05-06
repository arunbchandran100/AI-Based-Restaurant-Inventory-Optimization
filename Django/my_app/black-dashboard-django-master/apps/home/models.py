
from django.db import models
from django.contrib.auth.models import User

class FoodItem(models.Model):
    name = models.CharField(max_length=100)

class RawMaterial(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_type = models.CharField(max_length=50)


class Document(models.Model):
    uploaded_file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

