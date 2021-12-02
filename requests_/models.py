from django.db import models
import uuid


# ! Removal request

class ReturnRequest(models.Model):
    count = models.IntegerField(default=0, blank=False, null=False)
    finish_date = models.DateTimeField(blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=True)
