import json

from django.core.management import BaseCommand
from common.models import Country
from core.settings.base import BASE_DIR


class Command(BaseCommand):
    help = "Load all countries"

    def handle(self, *args, **kwargs):
        try:
            with open(str(BASE_DIR / "data/countries.json"), encoding="utf-8") as f:
                countries = json.load(f)
                for country in countries:
                    Country.objects.get_or_create(name=country['name_uz'], code=country['code'])

            self.stdout.write(self.style.SUCCESS("Countries load successfully"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error : {e}"))

# Barcha countrylarni bazaga qo'shib qo'yadi
