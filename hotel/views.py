from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Hotel


class HotelListView(ListView):
    model = Hotel
    template_name = 'hotel/hotel_list.html'
    context_object_name = 'hotels'
    queryset = Hotel.objects.prefetch_related('room_set').all()


class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'hotel/hotel_detail.html'