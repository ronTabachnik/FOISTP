from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from orders.models import Order, OrderItem
from items.models import Item
from requests_.models import ReturnRequest


def send_return_request_view(request, order_id):
    pass


@login_required
def list_return_requests_view(request):
    if not hasattr(request.user, 'business'):
        return redirect('login')
    user = request.user
    business = user.business
    return_requests = business.return_requests.all()
    print(return_requests)
    context = {
        'return_requests': return_requests,
        'current_user': user
    }
    return render(request, 'requests_/store_return_requests.html', context)


@login_required
def return_request_view(request, request_id):
    if not hasattr(request.user, 'business'):
        return redirect('login')
    user = request.user
    return_request = get_object_or_404(ReturnRequest, pk=request_id)
    context = {
        'return_request': return_request,
        'current_user': user
    }
    return render(request, 'requests_/store_return_request.html', context)


@login_required
def return_request_accept_view(request, request_id):
    if not hasattr(request.user, 'business'):
        return redirect('login')
    return_request = get_object_or_404(ReturnRequest, pk=request_id)
    return_request.status = ReturnRequest.Status.Accepted
    return_request.save()
    return redirect('store dashboard')


@login_required
def return_request_reject_view(request, request_id):
    if not hasattr(request.user, 'business'):
        return redirect('login')
    return_request = get_object_or_404(ReturnRequest, pk=request_id)
    return_request.status = ReturnRequest.Status.Rejected
    return_request.save()
    return redirect('store dashboard')


def crete_return_request_view(request, order_item_id):
    order_item = get_object_or_404(OrderItem, pk=order_item_id)
    return_request = ReturnRequest.objects.create(
        business=order_item.item.vendor,
        customer=order_item.order.customer,
        status=ReturnRequest.Status.Pending,
        order=order_item.order,
        item=order_item.item,
        count=order_item.quantity
    )
    return redirect('profile')
