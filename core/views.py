from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ContactForm

def home_view(request):
    return render(request, 'home.html')


class ContactView(CreateView):
    template_name = 'contactus_page.html'
    form_class = ContactForm
    success_url =  reverse_lazy('core:contact_view')