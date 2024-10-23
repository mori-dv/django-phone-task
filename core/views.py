from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DeleteView, TemplateView, DetailView
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
class ReportsView(LoginRequiredMixin, TemplateView):
    template_name = 'core/reports.html'


# Search API View
class SearchAPIView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', None)
        print(query)
        if query:
            phones = Phone.objects.filter(brand__name__icontains=query)
            phones_data = [
                {
                    'id': phone.id,
                    'brand': phone.brand.name,
                    'model': phone.model,
                    'price': phone.price,
                    'color': phone.color,
                    'screen_size': phone.screen_size,
                    'status': phone.status,
                    'country_of_manufacture': phone.country_of_manufacture
                } for phone in phones
            ]
            return JsonResponse({'phones': phones_data}, safe=False)
        return JsonResponse({'error': 'No query provided'}, status=400)


# Search Template View
class SearchView(TemplateView):
    template_name = "core/search_brand.html"


class NationalityEqualCountryReportView(LoginRequiredMixin, View):
    model = Phone

    def get(self, request, *args, **kwargs):
        phones = self.model.objects.filter(brand__nationality=F("country_of_manufacture"))
        response = [
            {
                "brand": phone.brand.name,
                "brand nationality": phone.brand.nationality,
                "model": phone.model,
                "price": phone.price,
                "screen_size": phone.screen_size,
                "status": phone.status,
                "country_of_manufacture": phone.country_of_manufacture
            } for phone in phones
        ]
        return JsonResponse({"phones": response}, safe=False)


class KoreanBrandReportView(LoginRequiredMixin, View):
    model = Phone

    def get(self, context, *args, **kwargs):
        phones = self.model.objects.filter(brand__nationality__icontains='Korea')

        data = [
            {
                "brand": phone.brand.name,
                "brand nationality": phone.brand.nationality,
                "model": phone.model,
                "price": phone.price,
                "screen_size": phone.screen_size,
                "status": phone.status,
                "country_of_manufacture": phone.country_of_manufacture
            } for phone in phones]

        return JsonResponse({"phones": data}, safe=False)

