from django.db.models import fields
from rest_framework import serializers
from .models import Advisor, Booking, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ['id', 'name', 'profileUrl']


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ['id', 'bookingTime', 'user', 'advisor']


class GetBookingSerializer(serializers.ModelSerializer):
    advisor = serializers.CharField(source='advisor.name')
    advisorProfileUrl = serializers.CharField(source='advisor.profileUrl')
    advisorId = serializers.IntegerField(source='advisor.id')

    class Meta:
        model = Booking
        fields = ['advisor', 'advisorProfileUrl',
                  'advisorId', 'bookingTime', 'id']
