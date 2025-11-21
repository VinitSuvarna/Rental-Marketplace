from django.db import models
from django.contrib.auth.models import User

# Our Category "LEGO brick" definition!
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Our Item "LEGO brick" definition!
class Item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField()

    # Add this new ImageField!
    # It will store the image in the 'media/items/' directory.
    image = models.ImageField(upload_to='items/', blank=True, null=True)

    price_daily = models.DecimalField(max_digits=10, decimal_places=2)
    price_weekly = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_hourly = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    condition = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    stock_quantity = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name