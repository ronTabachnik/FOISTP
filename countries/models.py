from django.db import models
import uuid


# ? Flag

class Country(models.Model):
    name = models.CharField(max_length=200, unique=True,
                            blank=False, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name
