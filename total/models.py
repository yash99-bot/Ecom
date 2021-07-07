from django.db import models
import datetime


# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=100, default='')
    price = models.IntegerField(default = 0)
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='images/', default='',null=True, blank=True)

@staticmethod
def get_products_by_id(ids):
    return product.objects.filter(id__in=ids)


@staticmethod
def __str__(self):
    return self.products

class customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email  = models.EmailField(max_length=70,blank=True,unique=True)
    password = models.CharField(max_length=50)


def register(self):
    self.save()   

def isExists(self):
    if coutomer.objects.filter(email = self.email): 
        return True
        return False 

class order(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    price = models.IntegerField(default = 0)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    address = models.IntegerField(max_length = 50, default='', blank=True)
    phone = models.IntegerField(max_length = 50, default='', blank=True) 


    ''' for product in products:
        order = Order(customer=Customer(id=customer),
                      product = product,
                      price = product.price,
                      address = address,
                      phone = phone)

        print(order.placeorder()); '''


def placeOrder(self):
    self.save()

@staticmethod 
def get_orders_by_customer(customer_id):
    return order.objects.filter(customer = customer_id)




