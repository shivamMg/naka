from django.core.management.base import BaseCommand

from projects.models import Tag


class Command(BaseCommand):
    help = 'Delete redundant tags'

    def handle(self, *args, **options):
        self.stdout.write('Deleting redundant tags:')
        for tag in Tag.objects.all():
            if not tag.project_set.exists():
                self.stdout.write(' - %s' % tag.name)
                tag.delete()

        self.stdout.write(self.style.SUCCESS('DONE'))
