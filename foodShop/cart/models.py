from django.db import models
from shopHome.models import *
# Create your models here.
class cartlist(models.Model):
    cartid=models.CharField(max_length=250,unique=True)
    date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '{}'.format(self.cartid)

class item(models.Model):
    prod=models.ForeignKey(product,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quantity=models.IntegerField()


    def __str__(self):
        return '{}'.format(self.prod)

    def total(self):
        return self.prod.price*self.quantity
