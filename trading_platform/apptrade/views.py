from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from apptrade.models import *
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "register.html"

    success_url = "/api"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class CurrencyCreate(LoginRequiredMixin, CreateView):
    model = Currency
    fields = ('code', 'name')


class CurrencyUpdate(LoginRequiredMixin, UpdateView):
    model = Currency
    fields = ('code', 'name')


class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    fields = ('code', 'name', 'price', 'currency', 'details')


class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ('code', 'name', 'price', 'currency', 'details')


class WatchListCreate(LoginRequiredMixin, CreateView):
    model = WatchList
    fields = ('user', 'item')


class WatchListUpdate(LoginRequiredMixin, UpdateView):
    model = WatchList
    fields = ('user', 'item')


class WatchListDelete(LoginRequiredMixin, DeleteView):
    model = WatchList


class PriceCreate(LoginRequiredMixin, CreateView):
    model = Price
    fields = ('currency', 'item', 'price', 'date')


class PriceUpdate(LoginRequiredMixin, UpdateView):
    model = Price
    fields = ('currency', 'item', 'price', 'date')


class PriceDelete(LoginRequiredMixin, DeleteView):
    model = Price
