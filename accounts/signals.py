from datetime import datetime, timedelta
from django.db.models.signals import post_save
from django.dispatch import  receiver

from accounts.models import User, VerificationOpt
from accounts.utils import generate_code, send_email
from core.settings.base import OTP_CODE_ACTIVATION_TIME


@receiver(post_save, sender=User)
def create_verification_otp(sender, instance, created, **kwargs):
    if created:
        code = generate_code()
        VerificationOpt.objects.create(user=instance, type=VerificationOpt.VerificationType.REGISTER, code=code,
                                       expires_in=datetime.now() + timedelta(OTP_CODE_ACTIVATION_TIME))

        send_email(code=code, email=instance.email)
        print("Signal is working ")


        #dsgsdgds