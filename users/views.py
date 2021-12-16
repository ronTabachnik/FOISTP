import datetime

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm

from django.db import IntegrityError

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from countries.models import Country
from items.models import Item
from orders.models import Order, OrderItem
from users.models import Customer, CustomerAddress
from users.utils import add_to_cart, add_to_wishlist, remove_from_cart, remove_from_wishlist
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

# def register_view(request):
#     if request.method == 'POST':
        
#         formset = UserRegisterForm(request.POST)
#         if formset.is_valid():
#             pass
#             # save pls form in database
#     else:
#         formset = UserRegisterForm()

#     context = {
#         'formset': formset
#     }
#     return render(request, 'users/register.html', context)

# def change status


def register_as_business_view(request):
    if request.method == 'POST':
        formset = BusinessFrom(request.POST, request.FILES)
        if formset.is_valid():
            legal_name = formset.cleaned_data['legal_name']
            store_name = formset.cleaned_data['store_name']
            email = formset.cleaned_data['email']
            password = formset.cleaned_data['password']
            store_name = formset.cleaned_data['store_name']
            avatar = formset.cleaned_data['avatar']
            review, _ = User.objects.create_user()

            # .objects.get_or_create_us(
            #    user=registered_customer, item=item)
        #    pass
            # grade = form.cleaned_data['grade']
            # text = form.cleaned_data['text']
            # item = get_object_or_404(Item, pk=item_id)
            # review, _ = Review.objects.get_or_create(
            #     user=registered_customer, item=item)
            # review.grade = grade
            # review.text = text
            # review.save()
            # регистрация юзера
            # Создать бизнес на основе юзера
            # save pls form in database
            # save()
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
    if not hasattr(request.user, 'registered_customer'):
        return redirect('login')
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
    cart = registered_customer.cart

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

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,('reg Success!'))
            return redirect('')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{})

def login_view(request):
    if request.method == "POST":
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(request, username=username, password=password)
         if user is not None:
            login(request, user)
            return redirect('home')
         else:
             messages.success(request,("There was an error logging in! Please try again!"))
             return redirect('login')
    else:
        return render(request, 'users/login.html',{})

@login_required
def payment_view(request):
    pass
