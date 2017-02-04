from django.core.management.base import BaseCommand

from projects.helpers import capture_screenshot
from projects.models import Project


class Command(BaseCommand):
    help = 'Capture screenshot for Project Photo'

    def add_arguments(self, parser):
        parser.add_argument('project_id', nargs=1, type=int)

    def handle(self, *args, **options):
        project_id = options['project_id'][0]
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            self.stdout.write(self.style.ERROR('No project with that id'))
            return

        confirm = input('Capture screenshot for "%s"? (y,n): ' % project.name)
        if confirm[0] != 'y' and confirm[0] != 'Y':
            self.stdout.write(self.style.ERROR('Screenshot not captured'))
            return

        self.stdout.write('Capturing screenshot for "%s"' % project.name)
        capture_screenshot(project)
        self.stdout.write(self.style.SUCCESS('DONE'))
