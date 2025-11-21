from django.contrib import admin
from .models import Category, Item

# Register the Category model
admin.site.register(Category)

# Use a custom admin class for the Item model
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price_daily', 'is_active', 'created_at', 'owner', 'image') # Add 'image' here
    list_filter = ('category', 'is_active', 'created_at')
    search_fields = ('name', 'description', 'location')

    fieldsets = (
        (None, {
            'fields': ('owner', 'category', 'name', 'description', 'image') # Add 'image' here
        }),
        ('Pricing', {
            'fields': ('price_daily', 'price_weekly', 'price_hourly')
        }),
        ('Details', {
            'fields': ('condition', 'location', 'stock_quantity', 'is_active')
        }),
    )

# Register the Item model with the custom admin class
admin.site.register(Item, ItemAdmin)