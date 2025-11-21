from django.urls import path
from . import views # Import views from the current app (items)

# This is important! We give a namespace to our app's URLs.
# It helps avoid conflicts if other apps use the same URL names.
app_name = 'items' # <--- ADD THIS LINE!

urlpatterns = [
    # Path for the item listing page. We can access it at /items/
    path('', views.item_list, name='item_list'), # e.g., rentalmarketplace.com/items/
   
    # Path for a specific item's detail page.
    # <int:pk> tells Django to expect an integer and pass it as 'pk' to the view function.
    path('<int:pk>/', views.item_detail, name='item_detail'), # e.g., /items/1/, /items/5/
]
