from rest_framework import serializers
from datetime import datetime
from my_app.models import Turf

class ReservationSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    team_name=serializers.CharField()
    contact_no=serializers.CharField()
    reservation_date=serializers.DateField()
    reservation_time=serializers.TimeField()
    turf=serializers.PrimaryKeyRelatedField(queryset=Turf.objects.all())
    duration=serializers.DurationField()

    def validate(self,validated_data):
        reservation_date=validated_data.get("reservation_date")
        if reservation_date<datetime.today().date():
            raise serializers.ValidationError("Date should be valid")
        return validated_data
        