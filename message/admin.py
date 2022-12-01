from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'client')
    list_filter = ('status',)


admin.site.register(Message, MessageAdmin)
