from typing import Tuple
from django.http import response
from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers, status
from .serializers import AdvisorSerializer, BookingSerializer, GetBookingSerializer, UserSerializer
from .models import Advisor, Booking, User
import jwt

# Create your views here.


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        payload = {
            'id': serializer.data['id'],
        }

        token = jwt.encode(payload, 'secret',
                           algorithm='HS256')

        return Response({
            'jwt': token,
            'id': serializer.data['id']
        })


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        payload = {
            'id': user.id,
        }

        token = jwt.encode(payload, 'secret',
                           algorithm='HS256')

        return Response({
            'jwt': token,
            'id': user.id
        })


class AddAdvisorView(APIView):
    def post(self, request):
        serializer = AdvisorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class RetrieveAdvisorView(APIView):
    def get(self, request, **kwargs):
        advisors = Advisor.objects.all()
        serializer = AdvisorSerializer(advisors, many=True)
        return Response(serializer.data)


class BookACallView(APIView):
    def post(sefl, request, **kwargs):
        serializer = BookingSerializer(data=dict(kwargs, **request.data))
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class GetBookedCalls(APIView):

    def get(self, request, **kwargs):
        booking = Booking.objects.filter(user__id=kwargs['user'])

        serializer = GetBookingSerializer(booking, many=True)
        return Response(serializer.data)
