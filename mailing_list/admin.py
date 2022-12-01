from django.contrib import admin
from .models import MailingList


class MailingListAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'start_datetime', 'end_datetaime', 'phone_code_filter', 'tag_filter')
    list_filter = ('start_datetime', 'end_datetaime', 'phone_code_filter', 'tag_filter')


admin.site.register(MailingList, MailingListAdmin)
