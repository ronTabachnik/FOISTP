from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render


def profile(request):
    if not request.user.is_authenticated or not hasattr(request.user, 'registered_customer'):
        return redirect('login')
    User = get_user_model()
    user = User.objects.get(username=request.user)
    registered_customer = user.registered_customer
    context = {
        'username': user.username,
        'avatar': registered_customer.avatar
    }
    return render(request, 'users/profile.html', context)


def login(request):
    context = {}
    return render(request, 'users/login.html', context)


def register(request):
    context = {}
    return render(request, 'users/register.html', context)


def wishlist(request):
    if not request.user.is_authenticated or not hasattr(request.user, 'registered_customer'):
        print(request.user)
        return redirect('login')
    User = get_user_model()
    user = User.objects.get(username=request.user)
    registered_customer = user.registered_customer
    wishlist = registered_customer.wishlist.all()
    context = {
        'wishlist': wishlist
    }
    return render(request, 'users/wishlist.html', context)


def cart(request):
    context = {
        'cart': None
    }
    return render(request, 'users/cart.html', context)
