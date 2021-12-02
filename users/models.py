import os
from django.db import models
from django.contrib.auth.models import User
import uuid
from countries.models import Country


# ! Customer address should have many to one relation with customer

def get_customer_avatar_path(instance, filename):
    return os.path.join('users', str(instance.user), 'profile', filename)


def get_business_avatar_path(instance, filename):
    return os.path.join('users', str(instance.user), 'businesses', str(instance.store_name), 'emblems', filename)


class RegisteredCustomer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to=get_customer_avatar_path, default='images/default.jpg')
    ban_status = models.BooleanField(default=False)

    def __str__(self):
        return self.user


class Customer(models.Model):
    name = models.CharField(max_length=200, blank=False, null=True)
    surname = models.CharField(max_length=200, blank=False, null=True)
    contact_phone = models.CharField(max_length=15, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return f'{self.name} {self.surname}'


class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    street = models.CharField(max_length=200, blank=False, null=True)
    building = models.CharField(max_length=200, blank=False, null=True)
    settlement = models.CharField(max_length=200, blank=False, null=True)
    zip = models.CharField(max_length=200, blank=True, null=True)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, blank=False, null=True)
    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    class Meta:
        verbose_name_plural = 'Customer addresses'

    def __str__(self):
        return f'{self.customer} {self.zip}'


class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Business(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    store_name = models.CharField(max_length=200, blank=False, null=True)
    avatar = models.ImageField(
        upload_to=get_business_avatar_path, default='images/default.jpg')

    class Meta:
        verbose_name_plural = 'Businesses'

    def __str__(self):
        return f'{self.store_name} {self.user}'
