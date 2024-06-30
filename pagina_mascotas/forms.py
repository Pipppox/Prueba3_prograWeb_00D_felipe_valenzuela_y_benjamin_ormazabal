from django import forms
from .models import CarritoProducto

class AgregarProductoForm(forms.ModelForm):
    class Meta:
        model = CarritoProducto
        fields = ['cantidad']
        widgets = {
            'cantidad': forms.NumberInput(attrs={'min': 1})
        }


