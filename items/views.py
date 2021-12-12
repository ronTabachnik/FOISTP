from django.shortcuts import get_object_or_404, redirect, render
from items.models import Category, Item, Review
from .forms import ReviewForm


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


def review_view(request, item_id):
    if not hasattr(request.user, 'registered_customer'):
        return redirect('login')
    user = request.user
    registered_customer = user.registered_customer
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            grade = form.cleaned_data['grade']
            text = form.cleaned_data['text']
            item = get_object_or_404(Item, pk=item_id)
            review, _ = Review.objects.get_or_create(
                user=registered_customer, item=item)
            review.grade = grade
            review.text = text
            review.save()
        return redirect('item', item_id)
    else:
        form = ReviewForm()
    context = {'form': form}
    return render(request, 'items/review.html', context)
