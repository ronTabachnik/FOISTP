import datetime

from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from django.db import IntegrityError

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from countries.models import Country
from items.models import Item
from orders.models import Order, OrderItem
from users.models import Business, Customer, CustomerAddress, RegisteredCustomer
from users.utils import add_to_cart, add_to_wishlist, decrease_item_amount, increase_item_amount, remove_from_cart, remove_from_wishlist, change_status, remove_business, change_application_to_approval, reject_application
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


@login_required
def registered_users_view(request):
    if not hasattr(request.user, 'registered_customer'):  # admin
        return redirect('login')
    users = RegisteredCustomer.objects.all()[:20]
    context = {
        'businesses': users
    }
    # admin_DashBoard
    return render(request, 'ADMINorders/orders.html', context)


@login_required
def businesses_view(request):
    if not hasattr(request.user, 'registered_customer'):  # admin
        return redirect('login')
    businesses = Business.objects.all()[:20]
    context = {
        'businesses': businesses
    }
    # admin_DashBoard
    return render(request, 'ADMINorders/orders.html', context)


@login_required
def change_application_approval_view(request, user_id):
    if not hasattr(request.user, 'registered_customer'):  # admin
        return redirect('login')
    user_to_business = Business.objects.get(id=user_id)
    change_application_to_approval(user_to_business)
    return redirect('admin_dashboard')


@login_required
def reject_application_view(request, user_id):
    if not hasattr(request.user, 'registered_customer'):  # admin
        return redirect('login')
    user_to_business = Business.objects.get(id=user_id)
    reject_application(user_to_business)
    return redirect('admin_dashboard')


@login_required
def change_profile_status_view(request, user_id):
    if not hasattr(request.user, 'registered_customer'):  # admin
        return redirect('login')
    status = True  # True for ban
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
            user = User.objects.create_user(
                username=legal_name, password=password, email=email)
            business = Business.objects.create(user=user, contact_phone=contact_phone,
                                               store_name=store_name, avatar=avatar)
            business.save()
            send_mail(
                'Approval letter',
                'message, that you have registered as business',
                'company@example.com',
                [email],
                fail_silently=False,
            )
    else:
        formset = BusinessFrom()

    context = {
        'formset': formset
    }
    # using smtplib for emails
    return render(request, 'users/register-business.html', context)
#                            ¯\_(ツ)_/¯


def request_store_closure_view(request):
    if not hasattr(request.user, 'business'):
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
    messages.success(request, 'Item added to wishlist')
    return redirect('wishlist')


@login_required
def remove_from_wishlist_view(request, item_id):
    if not hasattr(request.user, 'registered_customer'):
        return redirect('login')
    user = request.user
    registered_customer = user.registered_customer
    remove_from_wishlist(registered_customer, item_id)
    messages.success(request, 'Item deleted from to wishlist')
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
    messages.success(request, 'Item added to cart')
    return redirect('cart')


@login_required
def decrease_item_amount_view(request, item_id):
    if not hasattr(request.user, 'registered_customer'):
        return redirect('login')
    user = request.user
    registered_customer = user.registered_customer
    decrease_item_amount(registered_customer, item_id)
    return redirect('cart')


@login_required
def increase_item_amount_view(request, item_id):
    if not hasattr(request.user, 'registered_customer'):
        return redirect('login')
    user = request.user
    registered_customer = user.registered_customer
    increase_item_amount(registered_customer, item_id)
    return redirect('cart')


@login_required
def remove_from_cart_view(request, item_id):
    if not hasattr(request.user, 'registered_customer'):
        return redirect('login')
    user = request.user
    registered_customer = user.registered_customer
    remove_from_cart(registered_customer, item_id)
    messages.success(request, 'Item removed from cart')
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
            print(customer)

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
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('reg Success!'))
            return redirect('')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {})


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(
                request, ("There was an error logging in! Please try again!"))
            return redirect('login')
    else:
        return render(request, 'users/login.html', {})


@login_required
def payment_view(request):
    pass


@login_required
def store_dashboard_view(request):
    if not hasattr(request.user, 'business'):
        return redirect('login')
    user = request.user
    business = user.business
    return_requests = business.return_requests.all()
    context = {
        'return_requests': return_requests,
        'current_user': user
    }
    return render(request, 'users/store_dashboard.html', context)
