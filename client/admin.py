from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'phone_code', 'tag')
    list_filter = ('phone_code', 'tag')


admin.site.register(Client, ClientAdmin)
