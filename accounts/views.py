from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from  accounts.serializers import *
from  accounts.models import *
from accounts.utils import send_email

class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializers

    # def perform_create(self, serializer):
    #     serializer.save()
    #     send_email(serializer.instance.otp_code, serializer.instance.email)


