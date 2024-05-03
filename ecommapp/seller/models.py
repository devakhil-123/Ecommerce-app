from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Products(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    price=models.IntegerField()
    image=models.ImageField(upload_to="product_images")
    options=(
        ('SmartPhone','SmartPhone'),
        ('Tablets','Tablets'),
        ('SmartWatch','SmarWatch'),
        ('laptop','laptop'),

    )
    categories=models.CharField(max_length=200,choices=options)
    stock=models.IntegerField()
    def __str__ (self):
        return self.title