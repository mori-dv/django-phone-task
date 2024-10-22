from django.urls import path
from django.views.generic import RedirectView

from .views import (
    PhoneCreateView,
    PhoneListView,
    PhoneUpdateView,
    PhoneDeleteView,

    BrandCreateView,
    BrandListView,
    BrandUpdateView,
    BrandDeleteView,

    PhoneReportView,
    BrandReportView,
)


app_name = 'core'
urlpatterns = [
    path('', RedirectView.as_view(pattern_name='core:phone_list')),
    path('phone/add/', PhoneCreateView.as_view(), name='add_phone'),
    path('phone/<int:pk>/', PhoneUpdateView.as_view(), name='edit_phone'),
    path('phone/delete/<int:pk>/', PhoneDeleteView.as_view(), name='delete_phone'),
    path('phone/', PhoneListView.as_view(), name='phone_list'),
    path('brand/add/', BrandCreateView.as_view(), name='add_brand'),
    path('brand/<int:pk>/', BrandUpdateView.as_view(), name='edit_brand'),
    path('brand/delete/<int:pk>/', BrandDeleteView.as_view(), name='delete_brand'),
    path('brand/', BrandListView.as_view(), name='brand_list'),

    path('report/phone/', PhoneReportView.as_view(), name='phone_report'),
    path('report/brand/', BrandReportView.as_view(), name='brand_report'),
]
