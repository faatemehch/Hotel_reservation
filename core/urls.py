from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('contact/', views.ContactView.as_view(), name='contact_view'),
    path('about-us/', views.AboutView.as_view(), name='about_view'),
]
