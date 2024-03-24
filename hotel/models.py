from django.db import models
from django.conf import settings
from django.urls import reverse
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
import os


def get_file_name_ext(file_path):
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, fileName):
    _, ext = get_file_name_ext(fileName)
    final_name = f'{instance.name}.{ext}'
    return f'hotels/{final_name}'


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=upload_image_path)
    phone_number = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    description = RichTextField()
    additional_info = RichTextField()
    tags = TaggableManager() 
    star_rating = models.DecimalField(decimal_places=1, max_digits=2)
    base_price = models.DecimalField(decimal_places=2, max_digits=4)
    created_at = models.DateTimeField(auto_now_add=True)
    modiefied_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("hotel:hotel_detail", kwargs={"slug": self.slug})


class Room(models.Model):
    ROOM_TYPES = (
        ('s', 'Single'),
        ('d', 'Double'),
        ('st', 'Suit'),
    )
    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES,default=ROOM_TYPES[0][0])
    base_price = models.DecimalField(decimal_places=2, max_digits=4)
    max_occupancy = models.PositiveSmallIntegerField()  # number of guests allowed
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modiefied_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.room_type


class Review(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True)
    writer = models.CharField(max_length=255)
    body = models.TextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    customer_rate = models.PositiveSmallIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    modiefied_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.hotel)


class Reservation(models.Model):
    RESERVATION_STATUS = (
        ('p', 'Paid'),
        ('u', 'Un paid'),
        ('c', 'cancelled'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=46,  null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    # hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=1, choices=RESERVATION_STATUS, default=RESERVATION_STATUS[1][0])

    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()

    is_check_in = models.BooleanField(default=False)
    is_check_out = models.BooleanField(default=False)

    guests = models.PositiveSmallIntegerField()  # PositiveSmallIntegerField: starts from  0 to 32767

    created_at = models.DateTimeField(auto_now_add=True)
    modiefied_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} | {self.room.hotel.name}"

    def total_price(self):
        return 0
