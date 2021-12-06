from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    return render(request, 'items/home.html', context=context)


def item(request, item):
    context = {}
    return render(request, 'items/item.html', context=context)
