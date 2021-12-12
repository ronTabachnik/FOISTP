import uuid
from django.db import models
from items.models import Item


class Order(models.Model):
    class Status(models.TextChoices):
        Shipped = '1', 'Shipped'
        Ordered = '2', 'Ordered'
        Delivered = '3', 'Delivered'
        Processing = '4', 'Processing'
        Error = '5', 'Error'
    last_status = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.Error)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return f'{self.created}: {self.status}'


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
