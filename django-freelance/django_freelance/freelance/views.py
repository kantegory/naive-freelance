from rest_framework.response import Response
from rest_framework import generics

from .models import *
from .serializers import *


class TicketListView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

