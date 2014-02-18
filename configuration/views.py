from market.models import MarketConfiguration
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, ModelFormMixin

class ConfigurationList(ListView):
    model = MarketConfiguration    
    template_name = 'configuration/configuration_list.html'
    
    def get_queryset(self):
        queryset = super(ConfigurationList, self).get_queryset().filter(belongs_to=self.request.user)        
        return queryset

class ConfigurationCreate(CreateView):
    model = MarketConfiguration
    template_name = 'configuration/configuration_form.html'
    success_url = reverse_lazy('configuration_list')
    fields = ['market','access_key', 'access_sign', 'active']
        
    def get_context_data(self, **kwargs):
        context = super(ConfigurationCreate, self).get_context_data(**kwargs)
        context['creating'] = True
        return context
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.belongs_to = self.request.user
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)
 
class ConfigurationUpdate(UpdateView):
    model = MarketConfiguration
    template_name = 'configuration/configuration_form.html'
    success_url = reverse_lazy('configuration_list')
    fields = ['access_key', 'access_sign', 'active']
    
    def get_queryset(self):
        return super(ConfigurationUpdate, self).get_queryset().filter(belongs_to=self.request.user)
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.belongs_to = self.request.user
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)
