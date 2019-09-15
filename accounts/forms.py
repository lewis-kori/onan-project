from django import forms
from .models import accounts

class accountCreateForm(forms.ModelForm):
    class Meta:
        model = accounts
        fields=['name','password']

class accountUpdateForm(forms.ModelForm):
    class Meta:
        model = accounts
        fields=['name','password']