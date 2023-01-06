from django import forms
from .models import customers

class nuevoclienteform(forms.ModelForm):
  class Meta:
    model=customers
    fields='__all__'