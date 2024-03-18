from django.shortcuts import render
from django.views.generic import ListView
from .models import Hotel


class HotelListView(ListView):
    model = Hotel
    template_name = 'hotel/hotel_list.html'
    context_object_name = 'hotels'
