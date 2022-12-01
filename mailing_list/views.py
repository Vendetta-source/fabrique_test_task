from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import MailingListSerializer
from .models import MailingList
from message.models import Message


# Create your views here.
class MailingListViewSet(viewsets.ModelViewSet):
    serializer_class = MailingListSerializer

    def get_queryset(self):
        return MailingList.objects.all()

    @action(detail=True, methods=['get'])
    def mailing_info(self, request, pk=None):
        queryset = self.get_queryset()
        mailing = get_object_or_404(queryset, pk=pk)
        serializer = MailingListSerializer(mailing)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def full_mailing_info(self, request):
        queryset = self.get_queryset()
        serializer = MailingListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

