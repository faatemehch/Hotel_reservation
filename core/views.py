from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import ContactForm


def home_view(request):
    return render(request, 'home.html')


class ContactView(CreateView):
    template_name = 'contactus_page.html'
    form_class = ContactForm
    success_url = reverse_lazy('core:contact_view')


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "About Us"
        return context

class ProfileView(TemplateView):
    template_name = 'account/profile.html'