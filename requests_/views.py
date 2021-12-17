from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from orders.models import Order
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


def crete_return_request_view(request, order_id, item_id, amount):
    order = get_object_or_404(Order, pk=order_id)
    item = get_object_or_404(Item, pk=item_id)
    return_request = ReturnRequest.objects.create(
        business=item.vendor, customer=order.customer, status=ReturnRequest.Status.Pending, order=order, item=item, count=amount)
