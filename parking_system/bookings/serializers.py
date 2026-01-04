from rest_framework import serializers
from .models import Booking
from parking.models import ParkingSlot


class BookingSerializer(serializers.ModelSerializer):
    slot_id = serializers.PrimaryKeyRelatedField(
        queryset=ParkingSlot.objects.filter(status='available'),
        source='slot',
        write_only=True
    )

    class Meta:
        model = Booking
        fields = [
            'id',
            'slot_id',
            'slot',
            'start_time',
            'end_time',
            'status',
        ]
        read_only_fields = ['slot', 'status']

    def create(self, validated_data):
        request = self.context['request']
        slot = validated_data['slot']

        # Reserve the slot
        slot.status = 'reserved'
        slot.save()

        booking = Booking.objects.create(
            user=request.user,
            slot=slot,
            start_time=validated_data['start_time'],
            end_time=validated_data['end_time'],
            status='active'
        )

        return booking
