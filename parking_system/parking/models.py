from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ParkingLot(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='parking_lots'
    )

    def __str__(self):
        return self.name


class ParkingSlot(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('reserved', 'Reserved'),
        ('occupied', 'Occupied'),
    ]

    parking_lot = models.ForeignKey(
        ParkingLot,
        on_delete=models.CASCADE,
        related_name='slots'
    )
    slot_number = models.CharField(max_length=20)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='available'
    )

    def __str__(self):
        return f"{self.parking_lot.name} - Slot {self.slot_number}"
