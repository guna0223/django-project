from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(max_length=500)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    thumbnail = models.ImageField(upload_to='products/thumbnails')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    
    @property
    def offer_price(self):
        return self.price -(self.price * self.discount/100)
    
    def __str__(self):
        return self.title

