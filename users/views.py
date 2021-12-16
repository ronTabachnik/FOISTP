import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from items.models import Item
from orders.models import Order
from users.models import Business, RegisteredCustomer
from users.utils import add_to_cart, add_to_wishlist, checkout, remove_from_cart, remove_from_wishlist, change_status
from users.forms import BusinessFrom


@login_required
def profile_view(request):
    if not hasattr(request.user, 'registered_customer'):
        return redirect('login')
    user = request.user
    registered_customer = user.registered_customer
    context = {
        'username': user.username,
        'avatar': registered_customer.avatar,
        'current_user': user,
    }
    return render(request, 'users/profile.html', context)


def login_view(request):
    context = {}
    return render(request, 'users/login.html', context)


def register_view(request):
    context = {}
    return render(request, 'users/register.html', context)

def change_profile_status_view(request, user_id):
    if not hasattr(request.user, 'admin_customer'):
        return redirect('login')
    status = True #True for ban
    reg_user = RegisteredCustomer.objects.get(id=user_id)
    change_status(reg_user, status)
    return redirect('admin_dashboard')


def register_as_business_view(request):
    if request.method == 'POST':
        formset = BusinessFrom(request.POST, request.FILES)
        if formset.is_valid():
            legal_name = formset.cleaned_data['legal_name']
            store_name = formset.cleaned_data['store_name']
            email = formset.cleaned_data['email']
            password = formset.cleaned_data['password']
            contact_phone = formset.cleaned_data['contact_phone']
            store_name = formset.cleaned_data['store_name']
            avatar = formset.cleaned_data['avatar']
            user = User.objects.create_user(username=legal_name, password=password, email=email)
            business = Business.objects.create(user=user,contact_phone=contact_phone,
            store_name=store_name,avatar=avatar)
            business.save()           

        else:
            formset = BusinessFrom()

    context = {
        'formset': formset
    }
    return render(request, 'users/register-business.html', context)




@login_required
def wishlist_view(request):
    if not hasattr(request.user, 'registered_customer'):
        return redirect('login')
    user = request.user
    registered_customer = user.registered_customer
    wishlist = registered_customer.wishlist.all()
    context = {
        'wishlist': wishlist,
        'current_user': user,
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


@login_required
def cart_view(request):
    if not hasattr(request.user, 'registered_customer'):
        return redirect('login')
    user = request.user
    registered_customer = user.registered_customer
    cart = registered_customer.cart
    if not cart:
        cart = Order.objects.create(status=Order.Status.In_cart)
        registered_customer.cart = cart
        registered_customer.save()
    context = {
        'cart': cart.items.all(),
        'current_user': user,
    }
    return render(request, 'users/cart.html', context)


@login_required
def add_to_cart_view(request, item_id):
    user = request.user
    registered_customer = user.registered_customer
    add_to_cart(registered_customer, item_id)
    return redirect('cart')


@login_required
def remove_from_cart_view(request, item_id):
    if not hasattr(request.user, 'registered_customer'):
        return redirect('login')
    user = request.user
    registered_customer = user.registered_customer
    remove_from_cart(registered_customer, item_id)
    return redirect('cart')


@login_required
def checkout_view(request):
    if not hasattr(request.user, 'registered_customer'):
        return redirect('login')
    user = request.user
    registered_customer = user.registered_customer
    cart = registered_customer.cart.all()
    order = checkout(cart)

    # customer = Customer.objects.create(user=user)
    # customer.order = order
    # customer.save()

    context = {
        'order_items': order.items.all(),
        'current_user': user,
        # 'customer': customer
    }
    return render(request, 'users/checkout.html', context)

@login_required
def payment_view(request):
    pass
