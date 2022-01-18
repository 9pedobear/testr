from django import forms
from .models import *

class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employes
        fields = ['name', 'contact', 'email']
        widgets = {
            'name' : forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'contact': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Сюда номер телефона'}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control'}
            )
        }