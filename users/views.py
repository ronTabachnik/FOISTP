from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def home(request):
    context = {}
    return render(request, 'users/home.html', context=context)


def wishlist(request):
    if not request.user.is_authenticated and request.user.registeredCustomer:
        return redirect('home')
    user = User.objects.get(username=request.user)
    registered_customer = user.registered_customer
    wishlist = registered_customer.wishlist.all()
    context = {'wishlist': wishlist}
    return render(request, 'users/wishlist.html', context=context)
