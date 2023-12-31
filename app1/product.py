from django.db import models
from . models import Category
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=50)
    image=models.ImageField(upload_to='Uploads/product/')