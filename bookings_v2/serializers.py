from rest_framework import serializers
from django.contrib.auth.models import User
from bookings_v2.models import Reservation
from datetime import timedelta,time,datetime


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=["username","email","password"]


class ReservationSerializer(serializers.ModelSerializer):
    turf=serializers.StringRelatedField()
    class Meta:
        model=Reservation
        fields="__all__"
        read_only_fields=["id","end_time"]

    def validate(self,validated_data):
        duration=validated_data.get("duration")
        reservation_time=validated_data.get("reservation_time")
        reservation_date=validated_data.get("reservation_date")
        
        if duration<timedelta(hours=1):
            raise serializers.ValidationError("Duartion should be atleast 1 hour")
       

        start_datetime=datetime.combine(reservation_date,reservation_time)
        end_datetime=start_datetime+duration

        booking_start=time(8,0)
        booking_end=time(22,0)

        if start_datetime.time()<booking_start or end_datetime.time()>booking_end:
            raise serializers.ValidationError("Bookings should be between 8.00 AM and 10.00 PM")
         

        return validated_data

      
    
        

    
        
