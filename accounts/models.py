from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from accounts.managers import UserManager
from accounts.utils import check_otp_code


# Create your models here.
class User(AbstractUser):
    email = models.EmailField("Email", unique=True)
    phone_number = models.CharField('Phone Number', max_length=20, validators=[RegexValidator(r'^\+?1?\d{9,15}$')])
    address = models.TextField('Address')
    username = models.CharField(_("username"), max_length=150,
                                error_messages={"uniqeu": _("A user with that username already exists")}, null=True, blank=True)
    USERNAME_FIELD = 'email'
    objects = UserManager()
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"



class VerificationOpt(models.Model):
    class VerificationType(models.TextChoices):
        REGISTER = 'register', _('Register')
        RESET_PASSWORD = 'reset_password', _("Reset password")
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='verification_otp')
    code = models.IntegerField(_('Otp code'), validators=[check_otp_code])
    type = models.CharField(_('Verification Type'), max_length=60, choices=VerificationType.choices)
    expires_in = models.DateTimeField(_('Expires in'))


    def __str__(self):
        return f"{self.user.email} | code : {self.code}"


    class Meta:
        verbose_name = _('Verification Opt')
        verbose_name_plural = _('Verification Opts')


class UserAddress(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='user_addresses')
    name = models.CharField(_('Name'),max_length=50)
    phone_number = models.CharField(_('Phone Number'), max_length=20, validators=[RegexValidator(r'^\+?1?\d{9,15}$')])
    apartment = models.CharField(_('Apartment'), max_length=120)
    street = models.TextField(_('Street'))
    pin_code = models.CharField(_('Pin Code'), max_length=120)
    # city = models.ForeignKey(_('City'), )


    def __str__(self):
        return str(str(self.user.id) + " " + self.name)


    class Meta:
        verbose_name = _('User Address')
        verbose_name_plural = _('User Addresses')