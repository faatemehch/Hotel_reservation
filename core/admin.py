from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'is_staff', 'is_active')
    list_per_page = 10
    search_fields = ('username', 'email')
    list_display_links = ('id','username')

admin.site.register(CustomUser, CustomUserAdmin)