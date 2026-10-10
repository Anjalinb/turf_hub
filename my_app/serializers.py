from rest_framework import serializers

class TurfSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    fee=serializers.IntegerField()
    location=serializers.CharField()
    phone_no=serializers.CharField()

    def validate(self,validated_data):
        fee=validated_data.get("fee")
        if fee<500:
            raise serializers.ValidationError("Invalid fee! Fee should be greater than 300")
        return validated_data

class UserSerializer(serializers.Serializer):
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()