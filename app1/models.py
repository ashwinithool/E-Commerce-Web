

from django.db import models
import datetime





# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    category=models.ForeignKey("Category", on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=200,default='',null=True,blank=True)
    image=models.ImageField(upload_to='Uploads/product/')

    def __str__(self):
         return self.name


   

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
         return self.name

class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=500)


    @staticmethod
    def get_cutomer_by_email(email):
        Customer.objects.filter(email=email)

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False

class Order(models.Model):
    product=models.ForeignKey("Product", on_delete=models.CASCADE)

    customer=models.ForeignKey("Customer", on_delete=models.CASCADE)

    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.CharField(max_length=500,default='',blank=True)
    phone=models.CharField(max_length=20,default='',blank=True)
    date=models.DateField(default=datetime.datetime.today)

    

    
objects=models.Manager()

#def Exists(self):
 # if Customer.objects.filter(email=self.email):
  #  return True
  
  #return False

    