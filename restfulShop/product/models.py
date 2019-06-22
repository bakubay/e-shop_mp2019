from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    #product = models.ForeignKey(Product2, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
