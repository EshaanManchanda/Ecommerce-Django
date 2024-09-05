from django.utils import timezone
from django.db import models
from shop.models import Item as Product
from django.contrib.auth.models import User

# Create your models here.
class ProductInteraction(models.Model):
    
    INTERACTION_CHOICES = [
        ('view', 'View'),
        ('click', 'Click'),
        ('purchase', 'Purchase'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=10, choices=INTERACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} {self.interaction_type} {self.product}"