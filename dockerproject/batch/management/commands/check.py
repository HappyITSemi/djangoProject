# for Debug Setting and For the Django-custom-Command
# SCRIPT -> manage.py
# Parameter => command
# working Directory = Project Directory
# PUSH insect at the Top
# python manage.py check -period 2021-03 -dir media/outdata -file abc.csv
import logging

from django.core.management import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = '[Usage] command -period 2021-03 -dir media/outdata -file abc.csv'

    def add_arguments(self, parser):
        parser.add_argument('-period', nargs='+', type=str)
        parser.add_argument('-dir', type=str)  # Registered Argument 'period'
        parser.add_argument('-file', type=str)  # nargs + -> must be at least 1
        parser.add_argument('-id', type=int)

    def handle(self, *args, **options):
        logger = logging.getLogger("django")
        logger.debug("check--debug--check")
        logger.error('check--error--check')

        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)

        print('Period= ', options['period'])
        print('dir= ', options['dir'])
        print('file=', options['file'])
        print('id= ', options['id'])
