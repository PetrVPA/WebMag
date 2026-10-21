from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Создает группу Модератор продуктов и назначает права'

    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name='Модератор продуктов')

        perms = Permission.objects.filter(
            content_type__app_label='catalog',
            codename__in=[
                'can_publish_product',
                'can_unpublish_product',
                'can_view_product',
                'can_delete_product',
                'can_create_product',
                'can_edit_product'
            ]
        )

        group.permissions.set(perms)

        if created:
            self.stdout.write(self.style.SUCCESS('Группа создана и права назначены!'))
        else:
            self.stdout.write(self.style.SUCCESS('Группа уже существовала, права обновлены.'))