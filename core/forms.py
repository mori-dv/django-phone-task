from django import forms
from .models import Phone, Brand


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = '__all__'
        widgets = {
            'status': forms.RadioSelect,
        }


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
