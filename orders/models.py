from email.policy import default
import uuid
from django import utils
from django.db import models
from items.models import Item
import datetime


class Order(models.Model):
    class Status(models.TextChoices):
        Shipped = '1', 'Shipped'
        Ordered = '2', 'Ordered'
        Delivered = '3', 'Delivered'
        Processing = '4', 'Processing'
        In_cart = '5', 'In cart'
        Error = '6', 'Error'
    last_status = models.DateField(blank=True, default=utils.timezone.now)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.Error)
    created = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField(default=0.0)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return f'{self.created}: {self.status}'

    def set_status(self, status):
        if self.status != status:
            self.status = status
            self.last_status = utils.timezone.now


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items')
    quantity = models.IntegerField(default=0, blank=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
