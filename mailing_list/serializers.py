from rest_framework import serializers
from .models import MailingList
from message.models import Message


class MailingListSerializer(serializers.ModelSerializer):
    failed = serializers.SerializerMethodField()
    sent = serializers.SerializerMethodField()
    proceeded = serializers.SerializerMethodField()

    class Meta:
        model = MailingList
        fields = '__all__'

    def get_failed(self, pk):
        return len(Message.objects.filter(message=pk, status='failed'))

    def get_sent(self, pk):
        return len(Message.objects.filter(message=pk, status='sent'))

    def get_proceeded(self, pk):
        return len(Message.objects.filter(message=pk, status='proceeded'))
