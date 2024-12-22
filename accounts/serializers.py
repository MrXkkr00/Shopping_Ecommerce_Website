
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from rest_framework import serializers

from accounts.models import User, VerificationOtp
from accounts.utils import generate_code, send_email
from core.settings import base


class UserCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')

    def create(self, validate_data):
        user = User.objects.filter(email=validate_data.get("email"), is_avtice = False)
        if user.exists():
            sms = VerificationOtp.objects.get(user=user, type = VerificationOtp.VerificationType.REGISTER,
                                              expires_in__lt = timezone.now(), is_active = True)

            if sms:
                sms.expires_in = timezone.now() + base.OTP_CODE_ACTIVATION_TIME
                code = generate_code()
                sms.code = code
                send_email(code = code, email = user.email)

        return self.create(self, validate_data)


class VerifyOTPSerializer(serializers.Serializer):
    code = serializers.IntegerField(required=True)
    email = serializers.EmailField( required=True)
    verify_type = serializers.ChoiceField(choices=VerificationOtp.VerificationType)



class ResetPasswordStartSerializer(serializers.Serializer):
    email = serializers.EmailField( required=True)


class ResetPasswordFinishSerializer(serializers.Serializer):
    email = serializers.EmailField( required=True)
    verification = serializers.IntegerField(required=True)
    password = serializers.CharField(required=True)
    password_confirm = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs.get('password')!=attrs.get('password_confirm'):
            raise serializers.ValidationError('Password do not match')

        return attrs

