import datetime


from django.core.mail import send_mail
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from countries.models import Country
from items.models import Item
from orders.models import Order, OrderItem
from users.models import Business, Customer, CustomerAddress, RegisteredCustomer
from users.utils import add_to_cart, add_to_wishlist, remove_from_cart, remove_from_wishlist, change_status, remove_business
from users.forms import BusinessFrom, UserRegisterForm, CustomerForm


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


@login_required
def change_profile_status_view(request, user_id):
    if not hasattr(request.user, 'registered_customer'):#admin
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
    #using smtplib for emails
    send_mail(
        'Approval letter',
        'message, that you have registered as business',
        'company@example.com',
        [email],
        fail_silently=False,
        )
    return render(request, 'users/register-business.html', context)

def request_store_closure_view(request):
    if not hasattr(request.user, 'registered_customer'):#business
        return redirect('login')
    business_user = request.user.business
    remove_business(business_user)
    return redirect('login')



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
    if cart and cart.status != Order.Status.In_cart:
        registered_customer.cart = None
        registered_customer.save()
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
    #order = checkout(cart)

    if request.method == 'POST':
        formset = CustomerForm(request.POST, request.FILES)
        if formset.is_valid():
            name = formset.cleaned_data['name']
            surname = formset.cleaned_data['surname']
            contact_phone = formset.cleaned_data['contact_phone']

            country, _ = Country.objects.get_or_create(
                name=formset.cleaned_data['country']
            )
            address, _ = CustomerAddress.objects.get_or_create(
                country=country,
                zip=formset.cleaned_data['zip'],
                street=formset.cleaned_data['street'],
                building=formset.cleaned_data['building'],
                settlement=formset.cleaned_data['settlement']
            )
            try:
                customer = Customer.objects.create(
                    user=user,
                    name=name,
                    surname=surname,
                    order=cart,
                    address=address,
                    contact_phone=contact_phone
                )
                cart.set_status(Order.Status.Processing)
                cart.save()
            except IntegrityError:
                print('customer alredy exists')
            return redirect('home')
    else:
        formset = CustomerForm()

    order_items = OrderItem.objects.filter(order=cart)
    context = {
        'current_user': user,
        'order_items': order_items,
        'total_price': cart.total_price,
        'formset': formset
    }
    return render(request, 'users/checkout.html', context)

@login_required
def payment_view(request):
    pass
