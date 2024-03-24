from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('writer', 'body', 'customer_rate')
        widgets = {
            'customer_rate' : forms.NumberInput(attrs={'min':1, 'max':5})
        }