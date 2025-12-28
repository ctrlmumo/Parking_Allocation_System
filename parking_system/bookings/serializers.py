from rest_framework import serializers
from .models import Booking
from parking.serializers import ParkingSlotSerializer
from parking.models import ParkingSlot

class BookingSerializer(serializers.ModelSerializer):
    slot = ParkingSlotSerializer(read_only=True)
    slot_id = serializers.PrimaryKeyRelatedField(
        queryset=ParkingSlot.objects.all(), write_only=True, source='slot' #provided a queryset argument to ensure the related object exists before creating records
    )

    class Meta:
        model = Booking
        fields = ['id', 'user', 'slot', 'slot_id', 'start_time', 'end_time', 'status']
        read_only_fields = ['user', 'start_time', 'end_time', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamically set queryset for slot_id
        from parking.models import ParkingSlot
        self.fields['slot_id'].queryset = ParkingSlot.objects.filter(status='available')

    def create(self, validated_data):
        slot = validated_data['slot']
        # Mark slot as reserved
        slot.status = 'reserved'
        slot.save()
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)