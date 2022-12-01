from django.db.models import Q
from notif_service.settings import URL_TOKEN, URL_SERVICE
from .models import MailingList
from client.models import Client
from message.models import Message
import requests

HEADERS = {
        'Authorization': f'Bearer {URL_TOKEN}',
        'Content-Type': 'application/json'}


def send(pk):
    mailings_list = MailingList.objects.filter(pk=pk).first()

    if mailings_list.tag_filter and mailings_list.phone_code_filter:
        clients = Client.objects.filter(Q(phone_code=mailings_list.phone_code_filter) | Q(tag=mailings_list.tag_filter))
    elif mailings_list.tag_filter:
        clients = Client.objects.filter(tag=mailings_list.tag_filter)
    else:
        clients = Client.objects.filter(phone_code=mailings_list.phone_code_filter)

    for client in clients:
        message = Message.objects.create(status='proceeded',
                                         message=mailings_list,
                                         client=client)
        data = {
            "id": message.pk,
            "phone": client.phone_number,
            "text": mailings_list.message
        }
        try:
            response = requests.post(url=URL_SERVICE + str(message.pk), headers=HEADERS, json=data)
            if response.status_code == 200:
                message.status = 'sent'
                message.save()
        except:
            message.status = 'failed'
            message.save()

