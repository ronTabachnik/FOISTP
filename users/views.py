from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from items.models import Item
from users.utils import add_to_wishlist, remove_from_wishlist


@login_required
def profile_view(request):
    if not hasattr(request.user, 'registered_customer'):
        return redirect('login')
    User = get_user_model()
    user = User.objects.get(username=request.user)
    registered_customer = user.registered_customer
    context = {
        'username': user.username,
        'avatar': registered_customer.avatar
    }
    return render(request, 'users/profile.html', context)


def login_view(request):
    context = {}
    return render(request, 'users/login.html', context)


def register_view(request):
    context = {}
    return render(request, 'users/register.html', context)


@login_required
def wishlist_view(request):
    if not hasattr(request.user, 'registered_customer'):
        return redirect('login')
    user = request.user
    registered_customer = user.registered_customer
    wishlist = registered_customer.wishlist.all()
    context = {
        'wishlist': wishlist
    }
    return render(request, 'users/wishlist.html', context)


@login_required
def add_to_wishlist_view(request, item_id):
    if not hasattr(request.user, 'registered_customer'):
        return redirect('login')
    user = request.user
    registered_customer = user.registered_customer
    item = get_object_or_404(Item, pk=item_id)
    add_to_wishlist(registered_customer, item)
    return redirect('wishlist')


@login_required
def remove_from_wishlist_view(request, item_id):
    if not hasattr(request.user, 'registered_customer'):
        return redirect('login')
    user = request.user
    registered_customer = user.registered_customer
    remove_from_wishlist(registered_customer, item_id)
    return redirect('wishlist')


def cart(request):
    context = {
        'cart': None
    }
    return render(request, 'users/cart.html', context)
