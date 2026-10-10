from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from django.contrib.auth.models import User

from my_app.models import Turf
from my_app.serializers import TurfSerializer,UserSerializer

class AdminRegisterView(APIView):

    def post(self,request):
        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            User.objects.create_superuser(**cleaned_data)
            return Response(data=cleaned_data)
        else:
            return Response(serializer_instance.errors)

class TurfListCreateView(APIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAdminUser]

    def get(self,request):
        qs=Turf.objects.all()
        serializer_instance=TurfSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=TurfSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            Turf.objects.create(**cleaned_data)
            return Response(data=cleaned_data)
        else:
            return Response(data=serializer_instance.errors)

class TurfRetrieveUpdateDeleteView(APIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAdminUser]
    
    def get(self,request,pk=None):
        qs=Turf.objects.get(id=pk)
        serializer_instance=TurfSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self,request,pk=None):
        form_data=request.data
        serializer_instance=TurfSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            Turf.objects.filter(id=pk).update(**cleaned_data)
            return Response(data=cleaned_data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk=None):
        Turf.objects.filter(id=pk).delete()
        return Response(data={"message":"record has been deleted"})


