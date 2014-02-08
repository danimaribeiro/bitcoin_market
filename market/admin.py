from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from django.contrib.auth.models import User

# Register your models here.
from market.models import Order
from market.models import Trade


class TradeAdmin(admin.ModelAdmin):
    fields = ['tid', 'date', 'amount', 'price', 'type', 'coin']
    list_display = ['tid', 'date', 'amount', 'price', 'type', 'coin']
    list_filter = ['type',  ('date', DateFieldListFilter), 'coin']
    search_fields = ['date']
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Order)
admin.site.register(Trade, TradeAdmin)
