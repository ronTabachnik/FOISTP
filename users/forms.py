from typing import Container
from django import forms


class BusinessFrom(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    email = forms.EmailField(
        max_length=255,
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        )
    )
    password = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    contact_phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    store_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    avatar = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={'class': 'form-control'}
        )
    )
