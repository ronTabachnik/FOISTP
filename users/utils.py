import datetime

import logging

from django.shortcuts import get_object_or_404
from items.models import Item
from orders.models import Order, OrderItem


def add_to_wishlist(registered_customer, item):
    registered_customer.wishlist.add(item)


def remove_from_wishlist(registered_customer, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        logging.error(
            f'Failed to remove item from the user {registered_customer.username} wishlist. (Item with id:{item_id} does not exists.)')
    registered_customer.wishlist.remove(item)


def add_to_cart(registered_customer, item_id):
    item = get_object_or_404(Item, pk=item_id)
    cart = registered_customer.cart
    if not cart:
        cart = Order.objects.create(status=Order.Status.In_cart)
        registered_customer.cart = cart
        registered_customer.save()
    order_item, _ = OrderItem.objects.get_or_create(item=item, order=cart)
    order_item.quantity += 1
    order_item.save()


def remove_from_cart(registered_customer, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        logging.error(
            f'Failed to remove item from the user {registered_customer.username} cart. (Item with id:{item_id} does not exists.)')
    registered_customer.cart.remove(item)


def checkout(cart):
    order = Order.objects.create(
        last_status=datetime.datetime.now(),
        status=Order.Status.Processing)
    order.save()
    order.items.add(*cart)
    return order
