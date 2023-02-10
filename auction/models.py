from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Auction_details(models.Model):
    start_date = models.DateField(editable=True)
    end_time = models.DurationField()
    auction_on = models.BooleanField(default=False)

class Registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    phone  = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name
    

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Bidder(User):
 
    def __str__(self):
        return self.first_name

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.TextField(max_length=1000)
    product_thumbnail = models.ImageField()
    bidders = models.ManyToManyField(Bidder,related_name="bidders",blank=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    bid_start_price = models.IntegerField()
    bid_gap =  models.IntegerField(default=0)
    post_time = models.DateTimeField(auto_now=True)
    on_auction = models.BooleanField(default=False)
    bidding_starts = models.DateTimeField(editable=True,blank=True,null=True)
    bidding_ends = models.DateTimeField(editable=True,blank=True,null=True)

    def __str__(self) -> str:
        return self.product_name

class Onsale(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.TextField(max_length=1000)
    product_thumbnail = models.ImageField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    price = models.IntegerField()
    post_time = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.product_name

class Bidds(models.Model):
    bid_product = models.ForeignKey(Product,on_delete=models.CASCADE)
    bidder = models.CharField(max_length=100,default="me")
    bid_price = models.IntegerField()
    bid_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s - %s' % (self.bid_product.product_name,self.bidder)

    @property
    def highest_bid(self):
        hb = self.bid_price
        max(hb)
        return hb



class Product_img(models.Model):
    images = models.ImageField()
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.product_id.product_name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email    



