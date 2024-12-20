from rest_framework import serializers

from accounts.models import User


class UserCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')

