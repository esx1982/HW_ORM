import csv
from demo.models import Phone
from django.core.management.base import BaseCommand
from django.utils.text import slugify

ph = Phone()

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', newline='') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                ph.id = row['id']
                ph.name = row['name']
                ph.image = row['image']
                ph.price = row['price']
                ph.release_date = row['release_date']
                ph.lte_exists = row['lte_exists']
                ph.slug = slugify(row['name'])
                ph.save()
                print('all done!')
                pass

# c1 = Command
# c1.handle('phones.csv')
