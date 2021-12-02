import uuid
from django.db import models
from items.models import Item
from users.models import Customer


class OrderStatus(models.Model):
    status = models.CharField(
        max_length=200, unique=True, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=True)

    def __str__(self):
        return self.status


class Order(models.Model):
    last_status = models.DateField(blank=True, null=True)
    items = models.ManyToManyField(Item)
    status = models.ForeignKey(
        OrderStatus, on_delete=models.SET_NULL, blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=True)

    def __str__(self):
        return f'{self.customer}: {self.status}'
