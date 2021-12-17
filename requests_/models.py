from django.db import models
import uuid
from users.models import Business, Customer

# ! Removal request


class ReturnRequest(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    count = models.IntegerField(default=0, blank=False, null=False)
    finish_date = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=True)
