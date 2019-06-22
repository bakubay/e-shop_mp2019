from django.db import models

# Create your models here.
class Order(models.Model):
    PAYED = 'PO'
    PENDING = 'PE'
    CANCELLED = 'CA'

    STATUS_CHOICES = [(PAYED,'PO'),(PENDING, 'PE'),(CANCELLED,'CA')]

    userid = models.IntegerField()
    productid = models.IntegerField()
    status = models.CharField(max_length =2, choices=STATUS_CHOICES, default = PENDING,)
