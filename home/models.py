from audioop import reverse
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

import books
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    image = models.ImageField( null=False,blank=False)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True, null=False)
    isbn = models.CharField(max_length=17, default=True)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100, default=True)
    is_publisher = models.BooleanField(default = True)
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    book_available_count = models.IntegerField(default=0)
    
    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={
            "pk" : self.pk
        })
    def __str__(self):
        return self.title


    
class Student(models.Model):
    user = models.OneToOneField(User,null=True,blank=False,on_delete=models.CASCADE)
    stud_id = models.CharField(max_length=5)
    email = models.EmailField()

    def __str__(self):
        return self.user.username
    

class OrderItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.book.title}"
    
    
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField()
    order_id = models.CharField(max_length=100,unique=True,default=None,blank=True,null=True)

    def __str__(self):
        return self.user.username

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.book.discounted_price
