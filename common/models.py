from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Media(models.Model):
    class MediaType(models.TextChoices):
        IMAGE = 'image', _("Image")
        FILE = 'file', _("File")
        MUSIC = 'music', _("Music")
        VIDEO = 'video', _("Video")
    file = models.FileField(_('File'), upload_to='/files')
    type = models.CharField(_('Media Type'),max_length=60, choices=MediaType.choices)


    def __str__(self):
        return self.id


class Settings