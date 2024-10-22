from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Phone, Brand
from .forms import PhoneForm, BrandForm

import logging

logger = logging.getLogger(__name__)


# ####### Phone CRUD Actions ########
class PhoneCreateView(LoginRequiredMixin, CreateView):
    form_class = PhoneForm
    template_name = 'core/add_phone.html'
    model = Phone
    success_url = '/'

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect(self.success_url)

    def form_invalid(self, form):
        logger.error(f"Form errors: {form.errors}")
        return render(self.request, self.template_name, {'form': form, 'errors': form.errors})


class PhoneListView(ListView):
    model = Phone
    template_name = "core/list_phone.html"
    context_object_name = 'phones'


class PhoneUpdateView(LoginRequiredMixin, UpdateView):
    model = Phone
    form_class = PhoneForm
    template_name = 'core/update_phone.html'
    success_url = '/'

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect(self.success_url)

    def form_invalid(self, form):
        logger.error(f"Form errors: {form.errors}")
        return render(self.request, self.template_name, {'form': form, 'errors': form.errors})


class PhoneDeleteView(LoginRequiredMixin, DeleteView):
    model = Phone
    success_url = '/'
    template_name = "core/phone_confirm_delete.html"


# ####### Brand CRUD Actions ########
class BrandCreateView(LoginRequiredMixin, CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'core/add_brand.html'
    success_url = '/'

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect(self.success_url)

    def form_invalid(self, form):
        logger.error(f"Form errors: {form.errors}")
        return render(self.request, self.template_name, {'form': form, 'errors': form.errors})


class BrandListView(ListView):
    model = Brand
    context_object_name = 'brands'
    template_name = "core/list_brand.html"


class BrandUpdateView(LoginRequiredMixin, UpdateView):
    form_class = BrandForm
    template_name = 'core/update_brand.html'
    model = Brand
    success_url = '/'

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect(self.success_url)

    def form_invalid(self, form):
        logger.error(f"Form errors: {form.errors}")
        return render(self.request, self.template_name, {'form': form, 'errors': form.errors})


class BrandDeleteView(LoginRequiredMixin, DeleteView):
    model = Brand
    success_url = '/'
    template_name = 'core/brand_confirm_delete.html'


# ########### Reports #############
class PhoneReportView(LoginRequiredMixin, ListView):
    model = Phone

    def render_to_response(self, context, **response_kwargs):
        phones = Phone.objects.select_related('brand').all().values(
            'brand__name', 'model', 'price', 'color', 'screen_size', 'status', 'country_of_manufacture'
        )
        return JsonResponse(list(phones), safe=False)


class BrandReportView(LoginRequiredMixin, ListView):
    model = Brand

    def render_to_response(self, context, **response_kwargs):
        brands = Brand.objects.prefetch_related('phones').all().values('name', 'nationality')
        return JsonResponse(list(brands), safe=False)

