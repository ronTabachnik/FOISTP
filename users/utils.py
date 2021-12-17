import datetime

import logging

from django.shortcuts import get_object_or_404
from items.models import Item
from orders.models import Order, OrderItem
from users.models import Business


def add_to_wishlist(registered_customer, item):
    registered_customer.wishlist.add(item)


def remove_business(business):
    try:
        business.delete()
    except Business.DoesNotExist:
        logging.error(
            f'Failed to remove business {business.username} ')


def change_application_to_approval(user):
    try:
        user.approved = True
        user.save()
    except user.DoesNotExist:
        logging.error(
            f'Failed to change user')


def reject_application(user):
    try:
        remove_business(user)
        user.save()
    except user.DoesNotExist:
        logging.error(
            f'Failed to change user')


def change_status(user, status):
    try:
        user.ban_status = status
        user.save()
    except user.DoesNotExist:
        logging.error(
            f'Failed to change user')


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
    if cart and cart.status != Order.Status.In_cart:
        registered_customer.cart = None
        registered_customer.save()
        cart = registered_customer.cart
    if not cart:
        cart = Order.objects.create(status=Order.Status.In_cart)
        registered_customer.cart = cart
        registered_customer.save()
    order_item, _ = OrderItem.objects.get_or_create(item=item, order=cart)
    order_item.quantity += 1

    cart.save()
    order_item.save()


def increase_item_amount(registered_customer, item_id):
    try:
        item = OrderItem.objects.get(pk=item_id)
    except OrderItem.DoesNotExist:
        logging.error(
            f'Failed to increase item quantity in the user {registered_customer.user.username} cart. (Item with id:{item_id} does not exists.)')
    item.quantity += 1
    item.save()


def decrease_item_amount(registered_customer, item_id):
    try:
        item = OrderItem.objects.get(pk=item_id)
    except OrderItem.DoesNotExist:
        logging.error(
            f'Failed to decrease item quantity in the user {registered_customer.user.username} cart. (Item with id:{item_id} does not exists.)')
    item.quantity -= 1
    if item.quantity <= 0:
        item.delete()
    else:
        item.save()


def remove_from_cart(registered_customer, item_id):
    try:
        item = OrderItem.objects.get(pk=item_id)
    except OrderItem.DoesNotExist:
        logging.error(
            f'Failed to remove item from the user {registered_customer.user.username} cart. (Item with id:{item_id} does not exists.)')
    item.delete()


def checkout(cart):
    order = Order.objects.create(
        last_status=datetime.datetime.now(),
        status=Order.Status.Processing)
    order.save()
    order.items.add(*cart)
    return order
