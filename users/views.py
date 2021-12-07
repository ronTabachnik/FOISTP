from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render


def login(request):
    context = {}
    return render(request, 'users/login.html', context=context)


def register(request):
    context = {}
    return render(request, 'users/register.html', context=context)


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
    return render(request, 'users/wishlist.html', context=context)
