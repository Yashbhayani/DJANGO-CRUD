from django import forms

from .models import Register, Product


class registerform(forms.ModelForm):
    class Meta:
        model=Register
        fields='__all__'

class proform(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'