from django.db import models
from core.models import Item
from django.contrib.auth.models import User


class Venders(models.Model):
    vender = models.OneToOneField(
        User, related_name='ven', on_delete=models.CASCADE)
    item = models.ManyToManyField(Item)

    def __str__(self):
        return self.vender.username
