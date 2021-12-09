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
    items = models.ManyToManyField(Item)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.Error)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=True)

    def __str__(self):
        return f'{self.created}: {self.status}'
