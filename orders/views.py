from django.shortcuts import get_object_or_404, redirect, render
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
