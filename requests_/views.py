from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


@login_required
def list_return_requests_view(request):
    if not hasattr(request.user, 'business'):
        return redirect('login')
    user = request.user


@login_required
def return_request_view(request, request_id):
    if not hasattr(request.user, 'business'):
        return redirect('login')
    user = request.user
