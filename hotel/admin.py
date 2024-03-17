from django.contrib import admin
from .models import Hotel, Room, Review, Reservation


class RoomInline(admin.TabularInline):
    model = Room
    fields = ('room_type', 'base_price', 'max_occupancy')
    extra = 1


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_active')
    inlines = (RoomInline, )
    search_fields = ('name',)
    prepopulated_fields = {
        'slug': ("name",),
    }
    list_per_page = 10
    search_fields = ('name',)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('__str__','hotel', 'base_price')
    list_filter = ('base_price',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'writer', 'is_active')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status', 'check_in_date',
                    'check_out_date', 'guests')
