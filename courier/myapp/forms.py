from django import forms

from .models import *


class CourierForm(forms.ModelForm):
    class Meta:
        model=CourierService
        fields='__all__'