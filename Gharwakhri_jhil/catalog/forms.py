from django import forms
from .models import Product
import os
from django.utils import timezone
from django.forms.widgets import ClearableFileInput

from .models import Subscriber



class SubscribeForm(forms.Form):
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email address'}),
    )
# forms.py

class OrderForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput)
    quantity = forms.IntegerField(min_value=1, max_value=10, initial=1)


class DefaultImageWidget(ClearableFileInput):
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        if not value:
            context['widget']['value'] = '/backendstatic/bassets/imgs/defaultimg.jpeg'
        return context

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['user'].disabled = True
        self.fields['user'].initial = self.user

    class Meta:
        model = Product
        fields = ['name', 'selling_price', 'price', 'image', 'is_active', 'quantity', 'description', 'meta_keywords', 'categories', 'user']
        widgets = {
            'user': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'product_name', 'placeholder': 'Product Name',}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'MRP',}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Your Price',}),
            'image': DefaultImageWidget(),#'image': forms.ClearableFileInput(attrs={'class': 'form-control'})   27th march23
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total Items',}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Product Description Here',}),
            'meta_keywords': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Snacks, Sweets',}),
            'categories': forms.Select(attrs={'class': 'form-select'}),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['name'] = cleaned_data['name'].strip()
        cleaned_data['meta_keywords'] = cleaned_data['meta_keywords'].strip()
        return cleaned_data
    
    # 27th march23
    def clean_image_field(self):
        data = self.cleaned_data['image_field']
        if not data:
            raise forms.ValidationError('Please select an image to upload.')
        return data
    
    def add_timestamps(self, commit=True):
        product = self.save(commit=False)
        if product.pk:
            product.updated_at = timezone.now()
        else:
            product.created_at = timezone.now()
            product.updated_at = product.created_at
        if commit:
            product.save()
        return product
    