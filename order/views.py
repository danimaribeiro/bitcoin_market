from market.models import Order
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin

# Create your views here.
class OrderList(ListView):
    model = Order    
    
    def get_queryset(self):
        queryset = super(OrderList, self).get_queryset().filter(belongs_to=self.request.user)        
        return queryset

class OrderCreate(CreateView):
    model = Order
    success_url = reverse_lazy('order_list')
    fields = ['price','amount', 'type', 'market']
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.belongs_to = self.request.user
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)
 
class OrderUpdate(UpdateView):
    model = Order
    success_url = reverse_lazy('order_list')
    fields = ['price','amount', 'type', 'market', 'sincronized', 'status']
    
    def get_queryset(self):
        return super(OrderUpdate, self).get_queryset().filter(belongs_to=self.request.user)
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.belongs_to = self.request.user
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)

class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')
    def get_queryset(self):
        return super(OrderUpdate, self).get_queryset().filter(belongs_to=self.request.user)