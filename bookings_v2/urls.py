from django.urls import path
from bookings_v2.views import SignUpView,ReservationListCreateView,ReservationRetrieveUpdateDeleteView

urlpatterns=[
    path('signup/',SignUpView.as_view()),
    path('reservations/',ReservationListCreateView.as_view()),
    path('reservations/<int:pk>/',ReservationRetrieveUpdateDeleteView.as_view()),
]