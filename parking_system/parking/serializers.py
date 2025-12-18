from rest_framework import serializers
from .models import ParkingLot, ParkingSlot

class ParkingSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSlot
        fields = ['id', 'slot_number', 'status']


class ParkingLotSerializer(serializers.ModelSerializer):
    slots = ParkingSlotSerializer(many=True, read_only=True)

    class Meta:
        model = ParkingLot
        fields = ['id', 'name', 'location', 'slots']
