from django.contrib import admin
from . import models

admin.site.register(models.RegisteredCustomer)
admin.site.register(models.Customer)
admin.site.register(models.CustomerAddress)
admin.site.register(models.Business)
