from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=6,decimal_places = 2)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now_add = True)
    
class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]
    first_name = models.TextField(max_lenght = 255)
    last_name = models.CharField(max_length =255)
    email = models.EmailField(max_length=255,unique=True) 
    phone = models.CharField(max_digits=255)
    birth_date = models.DateField(auto_now= True, null = True)  
    membership = models.CharField(max_length=255,Choice = MEMBERSHIP_CHOICES, default='B')