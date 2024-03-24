from django.contrib import admin
from .models import CustomUser, Contact


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'is_staff', 'is_active')
    list_per_page = 10
    search_fields = ('username', 'email')
    list_display_links = ('id','username')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'is_responsed')
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Contact, ContactAdmin)
