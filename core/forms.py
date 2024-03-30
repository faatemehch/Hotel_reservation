from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('full_name','email', 'subject', 'body')
        widgets = {
            'full_name' : forms.TextInput(attrs={'placeholder':'Your Name'}),
            'email' : forms.TextInput(attrs={'placeholder':'Your Email'}),
            'subject' : forms.TextInput(attrs={'placeholder':'Your Subject'}),
            'body' : forms.Textarea(attrs={'placeholder':'Your Message'}),
        }