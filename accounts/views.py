from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from  accounts.serializers import *
from  accounts.models import *

class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializers


