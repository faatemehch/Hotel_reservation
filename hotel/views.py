from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .models import Hotel, Room, Reservation
from .forms import ReviewForm
from django.db.models import Q


class HotelListView(ListView):
    model = Hotel
    template_name = 'hotel/hotel_list.html'
    context_object_name = 'hotels'
    queryset = Hotel.objects.prefetch_related('room_set').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Our Hotels"
        return context


class HotelDetailView(FormMixin, DetailView):
    model = Hotel
    template_name = 'hotel/hotel_detail.html'
    form_class = ReviewForm
    queryset = Hotel.objects.prefetch_related('room_set', 'review_set', 'tags')

    def get_success_url(self):
        return reverse("hotel:hotel_detail", kwargs={"slug": self.object.slug})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Save the review here
        review = form.save(commit=False)
        review.hotel = self.object
        review.save()
        return super().form_valid(form)


def check_available_hotels(request):
    if request.method == 'GET':
        city = request.GET.get('city')
        check_in_date = request.GET.get('check-in')
        check_out_date = request.GET.get('check-out')
        # hotels = Hotel.objects.filter(city=city, is_active=True)
        booked_rooms = Reservation.objects.filter(
            Q(check_in_date__lte=check_out_date, check_out_date__gt=check_in_date) |
            Q(check_in_date__lt=check_in_date, check_out_date__gte=check_out_date) &
            Q(status='p')
        )
        available_rooms = Room.objects.select_related('hotel').filter(
            hotel__city=city, is_available=True).exclude(id__in=booked_rooms)
        

        print(available_rooms)
        context = {
            "available_rooms" : available_rooms,

        }
        return render(request, 'hotel/search_result.html', context)
    return HttpResponse("Test")
