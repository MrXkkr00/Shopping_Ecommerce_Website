import secrets

from django.core.validators import ValidationError
from django.core.mail import send_mail

from core.settings.base import EMAIL_HOST


def check_otp_code(value):
    if len(str(value)) != 6:
        raise ValidationError("Otp must be 6 digits")


def send_email(code, email):
    message = f"Your OTP code is {code}"
    send_mail(subject="Registration OTP code", message=message, from_email=EMAIL_HOST, recipient_list=[email], fail_silently=False)


def generate_code():
    return secrets.choice(range(100000, 999999))