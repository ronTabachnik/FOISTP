import logging
from items.models import Item


def add_to_wishlist(user, item):
    user.wishlist.add(item)


def remove_from_wishlist(user, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        logging.error(
            f'Failed to remove item from the user {user.username} wishlist. (Item with id:{item_id} does not exists.')
    user.wishlist.remove(item)
