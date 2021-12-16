import os
from django.db import models
from django.contrib.auth.models import User
import uuid
from countries.models import Country
from items.models import Item
from orders.models import Order


# ! Customer address should have many to one relation with customer

def get_customer_avatar_path(instance, filename):
    return os.path.join('users', str(instance.user), 'profile', filename)


def get_business_avatar_path(instance, filename):
    return os.path.join('users', str(instance.user), 'businesses', str(instance.store_name), 'emblems', filename)


class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class CustomerAddress(models.Model):
    street = models.CharField(max_length=200, blank=False, null=True)
    building = models.CharField(max_length=200, blank=False, null=True)
    settlement = models.CharField(max_length=200, blank=False, null=True)
    zip = models.CharField(max_length=200, blank=True, null=True)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, blank=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    class Meta:
        verbose_name_plural = 'Customer addresses'

    def __str__(self):
        return f'{self.zip} {self.country}, {self.street}, {self.building}'


class RegisteredCustomer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='registered_customer')
    avatar = models.ImageField(
        upload_to=get_customer_avatar_path, default='images/default.jpg')
    wishlist = models.ManyToManyField(
        Item, blank=True, related_name='wishlist')
    cart = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    ban_status = models.BooleanField(default=False)
    saved_address = models.ForeignKey(
        CustomerAddress, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.user)


class Customer(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=200, blank=False, null=True)
    surname = models.CharField(max_length=200, blank=False, null=True)
    contact_phone = models.CharField(max_length=15, blank=True, null=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True)
    address = models.ForeignKey(CustomerAddress, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Business(models.Model):
    # default standart status myk
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    store_name = models.CharField(max_length=200, blank=False, null=True)
    avatar = models.ImageField(
        upload_to=get_business_avatar_path, default='images/default.jpg')

    class Meta:
        verbose_name_plural = 'Businesses'

    def __str__(self):
        return f'{self.store_name}'
