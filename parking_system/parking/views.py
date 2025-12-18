from django.shortcuts import render
from rest_framework import generics, permissions
from .models import ParkingLot, ParkingSlot
from .serializers import ParkingLotSerializer, ParkingSlotSerializer
from .permissions import IsParkingAdmin

# Create your views here.
class ParkingLotListCreateView(generics.ListCreateAPIView):
    queryset = ParkingLot.objects.all()
    serializer_class = ParkingLotSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsParkingAdmin()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ParkingLotDetailView(generics.RetrieveUpdateAPIView):
    queryset = ParkingLot.objects.all()
    serializer_class = ParkingLotSerializer
    permission_classes = [IsParkingAdmin]


class ParkingSlotListCreateView(generics.ListCreateAPIView):
    serializer_class = ParkingSlotSerializer
    permission_classes = [IsParkingAdmin]

    def get_queryset(self):
        return ParkingSlot.objects.filter(
            parking_lot_id=self.kwargs['lot_id']
        )

    def perform_create(self, serializer):
        serializer.save(parking_lot_id=self.kwargs['lot_id'])


class AvailableSlotsView(generics.ListAPIView):
    serializer_class = ParkingSlotSerializer

    def get_queryset(self):
        return ParkingSlot.objects.filter(status='available')
