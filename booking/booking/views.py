from rest_framework import generics

from .models import Booking
from .serializers import BookingSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwnerOrReadOnly


class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer