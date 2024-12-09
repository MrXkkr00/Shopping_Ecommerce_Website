from django.core.validators import ValidationError


def check_otp_code(value):
    if len(str(value)) != 6:
        raise ValidationError("Otp must be 6 digits")
