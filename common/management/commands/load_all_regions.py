import json

from django.core.management import BaseCommand
from common.models import Region, Country
from core.settings.base import BASE_DIR


class Command(BaseCommand):
    help = "Load all Regions"

    def handle(self, *args, **kwargs):
        try:
            with open(str(BASE_DIR / "data/regions.json"), encoding="utf-8") as f:
                regions = json.load(f)
                country = Country.objects.get(code="UZ")
                for region in regions:
                    Region.objects.get_or_create(name=region['name_uz'], country=country)

            self.stdout.write(self.style.SUCCESS("Regions load successfully"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error : {e}"))

# Barcha countrylarni bazaga qo'shib qo'yadi