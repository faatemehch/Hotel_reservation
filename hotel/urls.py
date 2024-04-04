from django.urls import path
from . import views

app_name = 'hotel'
urlpatterns = [
    path('', views.HotelListView.as_view(), name='hotel_list'),
    path('check_available_hotels/', views.check_available_hotels, name='check_available_hotels'),
    path('<slug>/', views.HotelDetailView.as_view(), name='hotel_detail'),
]
