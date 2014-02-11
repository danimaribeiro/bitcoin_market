from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from django.contrib.auth.models import User

# Register your models here.
from market.models import Order, Trade, Market, MarketConfiguration, Settings


class TradeAdmin(admin.ModelAdmin):
    fields = ['tid', 'date', 'amount', 'price', 'type', 'coin']
    list_display = ['tid', 'date', 'amount', 'price', 'type', 'coin']
    list_filter = ['type',  ('date', DateFieldListFilter), 'coin']
    search_fields = ['date']
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
class MarketConfigurationAdmin(admin.ModelAdmin):
    fields = ['market', 'access_key', 'access_sign']    
    list_display = ['market', 'access_key', 'access_sign', 'belongs_to']
    
    def save_model(self, request, obj, form, change): 
        instance = form.save(commit=False)        
        instance.belongs_to = request.user
        instance.save()
        form.save_m2m()
        return instance
    
    
class OrderAdmin(admin.ModelAdmin):
    fields = [ 'price', 'amount', 'type','market', 'status', 'sincronized']
    readonly_fields = ['status', 'sincronized']
    list_display = ['tid','price', 'amount', 'type','market', 'status', 'sincronized', 'belongs_to']
    
    
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return self.readonly_fields + ['market','price','amount', 'type']
        return self.readonly_fields
    
    def save_model(self, request, obj, form, change): 
        instance = form.save(commit=False)        
        instance.belongs_to = request.user
        instance.save()
        form.save_m2m()
        return instance

admin.site.register(Order, OrderAdmin)
admin.site.register(Market)
admin.site.register(MarketConfiguration, MarketConfigurationAdmin)
admin.site.register(Settings)
admin.site.register(Trade, TradeAdmin)
