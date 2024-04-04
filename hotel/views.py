from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .models import Hotel
from .forms import ReviewForm


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
    queryset = Hotel.objects.prefetch_related('room_set', 'review_set')

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
    if request.method == 'POST':
        city = request.POST['city']
        check_in_date = request.POST['check-in']
        check_out_date = request.POST['check-out']
        hotels = Hotel.objects.filter(city=city, is_active=True)
        print(hotels)
        context = {
            'hotels':hotels
        }
        return render(request, 'hotel/hotel_list.html', context)
    return HttpResponse("Test")