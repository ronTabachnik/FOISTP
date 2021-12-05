from django.shortcuts import render


def login(request):
    context = {}
    return render(request, 'users/login.html', context=context)


def register(request):
    context = {}
    return render(request, 'users/register.html', context=context)
