import os
import uuid
from django.db import models

from colors.models import Color


def get_category_picture_path(instance, filename):
    return os.path.join('categories', instance.name, 'images', filename)


def get_item_picture_path(instance, filename):
    return os.path.join('items', instance.title, 'images', filename)


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True,
                            blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(
        upload_to=get_category_picture_path, default='images/default.jpg')
    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=False, null=True)
    balance = models.IntegerField(default=0, blank=False)
    picture = models.ImageField(
        upload_to=get_item_picture_path, default='images/default.jpg')
    description = models.TextField(blank=True, null=True)
    size = models.IntegerField(default=0, blank=False)
    color = models.ForeignKey(
        Color, on_delete=models.SET_NULL, blank=True, null=True)
    material = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)
    manufacturer = models.CharField(max_length=200, blank=True, null=True)
    count_in_pack = models.IntegerField(default=0, blank=True, null=True)
    rating = models.DecimalField(
        max_digits=3, decimal_places=1, default=0.0, blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title
