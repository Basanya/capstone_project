from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title =  models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name="books", on_delete=models.CASCADE)
    isbn = models.CharField(max_length=20)
    pages = models.IntegerField()
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    imageurl = models.URLField(null=True)
    created_by = models.ForeignKey('auth.user',related_name='books', on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=False)

    class meta:
        ordering = ['date_created']

        def __str__(self):
            return self.title
        

class Product(models.Model):
    product_tag = models.CharField(max_length=15)
    name = models.CharField(max_length=120)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageurl = models.URLField(null=True)
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=False)            
    created_by = models.ForeignKey('auth.user',related_name='products', on_delete=models.CASCADE, null=True)
    
    class meta:
        ordering = ['date_created']

    def __str__(self):
        return '{} {}'.format(self.product_tag, self.name)


    