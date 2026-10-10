from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import authentication,permissions

from bookings_v2.serializers import SignUpSerializer,ReservationSerializer
from bookings_v2.models import Reservation

from datetime import datetime,time,timedelta

class SignUpView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=SignUpSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            user_object=User.objects.create_user(**cleaned_data)
            serializer_instance=SignUpSerializer(user_object)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class ReservationListCreateView(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):
        qs=Reservation.objects.all()
        serializer_instance=ReservationSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=ReservationSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            turf=cleaned_data.get("turf")
            reservation_date=cleaned_data.get("reservation_date")
            duration=cleaned_data.get("duration")
            reservation_time=cleaned_data.get("reservation_time")
            
            end_datetime=datetime.combine(reservation_date,reservation_time)+duration
            end_time=end_datetime.time()

            existing_bookings=Reservation.objects.filter(turf=turf,reservation_date=reservation_date,reservation_time__lt=end_time,end_time__gt=reservation_time).exists()
            if existing_bookings:
                return Response(data={"message":"Turf is already booked during the selected time"})

            qs=Reservation.objects.create(**cleaned_data,end_time=end_time)
            serializer_instance=(ReservationSerializer(qs))
            return Response(data=serializer_instance.data)

        else:
            return Response(data=serializer_instance.errors)


class ReservationRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    serializer_class=ReservationSerializer
    queryset=Reservation.objects.all()

