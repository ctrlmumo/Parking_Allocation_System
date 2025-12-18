from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Booking
from .serializers import BookingSerializer
from parking.models import ParkingSlot

# Create your views here.
class BookingCreateView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        return {'request': self.request}


class MyBookingsListView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class BookingDetailView(generics.RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookingCancelView(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.status = 'cancelled'
        instance.slot.status = 'available'
        instance.slot.save()
        instance.save()


class BookingCheckInView(generics.UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        booking = self.get_object()
        if booking.status != 'active':
            return Response({'error': 'Cannot check-in. Booking is not active.'}, status=status.HTTP_400_BAD_REQUEST)
        booking.status = 'active'
        booking.save()
        return Response(self.get_serializer(booking).data)


class BookingCheckOutView(generics.UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        booking = self.get_object()
        if booking.status != 'active':
            return Response({'error': 'Cannot check-out. Booking is not active.'}, status=status.HTTP_400_BAD_REQUEST)
        booking.status = 'completed'
        booking.end_time = timezone.now()
        booking.slot.status = 'available'
        booking.slot.save()
        booking.save()
        return Response(self.get_serializer(booking).data)
