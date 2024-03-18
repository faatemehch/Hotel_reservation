from django.urls import path
from . import views

app_name = 'hotel'
urlpatterns = [
    path('', views.HotelListView.as_view(), name='hotel_list'),
]
