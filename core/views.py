from django.shortcuts import render
from items.models import Item # Import the Item model

# Our homepage view function
def index(request):
    # Fetch the latest 4 active items to display as featured/trending
    featured_items = Item.objects.filter(is_active=True).order_by('-created_at')[:4]

    context = {
        'featured_items': featured_items,
    }
    return render(request, 'core/homepage.html', context)