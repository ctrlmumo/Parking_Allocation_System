from django.urls import path
from .views import (
    BookingCreateView,
    MyBookingsListView,
    BookingDetailView,
    BookingCancelView,
    BookingCheckInView,
    BookingCheckOutView,
)

urlpatterns = [
    path('booking/create/', BookingCreateView.as_view()),
    path('booking/my/', MyBookingsListView.as_view()),
    path('booking/<int:pk>/', BookingDetailView.as_view()),
    path('booking/<int:pk>/cancel/', BookingCancelView.as_view()),
    path('booking/<int:pk>/check-in/', BookingCheckInView.as_view()),
    path('booking/<int:pk>/check-out/', BookingCheckOutView.as_view()),
]
