from django.shortcuts import render, get_object_or_404
from .models import Item, Category
from django.contrib.auth.models import User

# View to display a list of items
def item_list(request):
    items = Item.objects.filter(is_active=True)
    category_id = request.GET.get('category')

    if category_id:
        try:
            selected_category = Category.objects.get(pk=category_id)
            items = items.filter(category=selected_category)
        except Category.DoesNotExist:
            pass

    items = items.order_by('-created_at')
    categories = Category.objects.all().order_by('name')
    results_count = items.count()

    context = {
        'items': items,
        'categories': categories,
        'results_count': results_count,
        'selected_category_id': category_id,
    }
    return render(request, 'items/item_list.html', context)

# View to display a single item's details
def item_detail(request, pk): # 'pk' is the primary key (ID) passed in the URL
    item = get_object_or_404(Item, pk=pk, is_active=True)

    context = {
        'item': item,
    }
    return render(request, 'items/item_detail.html', context)