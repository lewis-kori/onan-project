from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView, ListView
from .models import accounts
from .forms import accountCreateForm,accountUpdateForm

# Create your views here.

class index(ListView):
    template_name = "accounts/index.html"
    model = accounts
    context_object_name = "accounts"

class accountCreate(CreateView):
    model = accounts
    form_class = accountCreateForm
    template_name = 'accounts/updateAccount.html'

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)


class updateAccount(UpdateView):
    model = accounts
    form_class = accountUpdateForm
    template_name = 'accounts/updateAccount.html'
    uccess_url="/"
    
class deleteAccount(DeleteView):
    model = accounts
    success_url="/"
    template_name= 'accounts/confirm_delete.html'
    