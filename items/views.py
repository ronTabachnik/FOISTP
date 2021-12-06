from django.shortcuts import render

from items.models import Item

# Create your views here.


def home(request):
    items = Item.objects.all()[:20]

    context = {
        'items': items
    }
    return render(request, 'items/home.html', context=context)


def item_detail(request, item):
    context = {}
    return render(request, 'items/item.html', context=context)
