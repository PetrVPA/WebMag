from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Add test data to the database django_project'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()