import datetime

import logging
from items.models import Item
from orders.models import Order


def add_to_wishlist(registered_customer, item):
    registered_customer.wishlist.add(item)


def remove_from_wishlist(registered_customer, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        logging.error(
            f'Failed to remove item from the user {registered_customer.username} wishlist. (Item with id:{item_id} does not exists.)')
    registered_customer.wishlist.remove(item)


def add_to_cart(registered_customer, item):
    registered_customer.cart.add(item)


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