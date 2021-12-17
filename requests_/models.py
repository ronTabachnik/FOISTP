from django.db import models
import uuid
from orders.models import Order
from users.models import Business, Customer
from items.models import Item
# ! Removal request


class ReturnRequest(models.Model):
    class Status(models.TextChoices):
        Pending = '1', 'Pending'
        Accepted = '2', 'Accepted'
        Rejected = '3', 'Rejected'
        Error = '4', 'Error'
    business = models.ForeignKey(
        Business, on_delete=models.CASCADE, related_name='return_requests')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.Error)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.IntegerField(default=0, blank=False, null=False)
    finish_date = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=True)
