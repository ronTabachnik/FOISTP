from django.contrib import admin
from . import models

admin.site.register(models.OrderStatus)
admin.site.register(models.Order)
