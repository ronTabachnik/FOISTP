from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Order
from users.models import Customer


@login_required
def orders_view(request):
    if not hasattr(request.user, 'registered_customer'):
        return redirect('login')
    user = request.user
    customers = Customer.objects.filter(user=user)
    orders = [customer.order for customer in customers]
    context = {
        'orders': orders
    }
    return render(request, 'orders/orders.html', context)


def order_detail_view(request, order_id):
    order = Order.objects.filter(pk=order_id).first()
    context = {
        'order': order
    }
    return render(request, 'orders/order.html', context)


@login_required
def store_orders_view(request):
    if not hasattr(request.user, 'business'):
        return redirect('login')
    user = request.user
    business = user.business
    items = business.item_set.all()
    orders = set()
    for item in items:
        orders.update(item.order_set.all())
    context = {
        'orders': orders
    }
    return render(request, 'orders/store_orders.html', context)


def store_order_detail_view(request, order_id):
    order = Order.objects.filter(pk=order_id).first()
    context = {
        'order': order
    }
    return render(request, 'orders/store_order.html', context)
