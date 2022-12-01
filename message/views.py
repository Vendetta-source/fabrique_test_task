from rest_framework import viewsets
from .serializers import MessageSerializer
from .models import Message


# Create your views here.
class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
