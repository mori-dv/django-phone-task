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

    ReportsView,
    NationalityEqualCountryReportView,
    KoreanBrandReportView,

    SearchView,
    SearchAPIView
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

    path("reports/", ReportsView.as_view(), name="reports"),
    path('reports/equal_nationality/', NationalityEqualCountryReportView.as_view(), name='equality_brand'),
    path("reports/korean/", KoreanBrandReportView.as_view(), name="korean_brand"),

    path('search/', SearchView.as_view(), name='search'),
    path('api/search/', SearchAPIView.as_view(), name='search_api'),
]
