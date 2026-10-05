from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Add test data to the database django_project'

    def handle(self, *args, **options):
        call_command('delet_data_bd')
        call_command('loaddata', 'category.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))
        call_command('loaddata', 'product.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))