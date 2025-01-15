from django.db import models


class Collection(models.Model):
    Name = models.CharField(max_length=255)
    
    
class Product(models.Model):
    title = models.Charfield(max_length=255)
    description = models.Textfield()
    price = models.DecimalField(max_digits=6,decimal_place=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection,on_delete = models.CASCADE)
    
class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_GOLD,'Gold')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.Charfiled(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=255,choices=MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONZE)
class Order(models.Model):
    PAYMENT_STATUS_ChOICE = [
        ('P','Pending'),
        ('C','Complete'),
        ('F','Failed')
    ]  
    placed_at = models.DateTimeField(auto_now=True)
    payment_status = models.CharField(max_length=255,Choices=PAYMENT_STATUS_ChOICE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    
    
class Address(models.Model):
    Street = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    
