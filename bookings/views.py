from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from bookings.models import Reservation
from bookings.serializers import ReservationSerializer

class ReservationListCreateView(APIView):
    def get(self,request):
        qs=Reservation.objects.all()
        serializer_instance=ReservationSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=ReservationSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            Reservation.objects.create(**cleaned_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class ReservationRetrieveUpdateDeleteView(APIView):

    def get(self,request,pk=None):
        qs=Reservation.objects.get(id=pk)
        serializer_instance=ReservationSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self,request,pk=None):
        form_data=request.data
        serializer_instance=ReservationSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            Reservation.objects.filter(id=pk).update(**cleaned_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk=None):
        Reservation.objects.get(id=pk).delete()
        return Response(data={"message":"record has been deleted"})
