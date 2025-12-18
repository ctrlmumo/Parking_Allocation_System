from django.urls import path
from .views import (
    ParkingLotListCreateView,
    ParkingLotDetailView,
    ParkingSlotListCreateView,
    AvailableSlotsView,
)

urlpatterns = [
    path('parking-lots/', ParkingLotListCreateView.as_view()),
    path('parking-lots/<int:pk>/', ParkingLotDetailView.as_view()),
    path('parking-lots/<int:lot_id>/slots/', ParkingSlotListCreateView.as_view()),
    path('slots/available/', AvailableSlotsView.as_view()),
]
