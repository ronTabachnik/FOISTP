from django.shortcuts import render
from items.models import Category, Item


def home_view(request):
    items = Item.objects.all()[:20]
    categories = Category.objects.all()
    context = {
        'items': items,
        'categories': categories,
    }
    return render(request, 'items/home.html', context)


def item_detail_view(request, item_id):
    context = {}
    try:
        item = Item.objects.get(pk=item_id)
        context['item'] = item
    except Item.DoesNotExist:
        context['error_message'] = 'Failed to fetch an item.'
    return render(request, 'items/item.html', context)
