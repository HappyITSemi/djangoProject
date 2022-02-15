# Publish - Subscribre Model -- Push Pop

from django.core.management import BaseCommand
from django.utils import timezone
import logging


class Command(BaseCommand):
    help = '[description] Publish-Subscribe Model Push-Pop'

    def add_arguments(self, parser):
        parser.add_argument('-period', nargs='+', type=str)
        parser.add_argument('-dir', type=str)  # Registered Argument 'period'

    def handle(self, *args, **options):
        logger = logging.getLogger(__name__)
        logger.level = logging.INFO
        logger.info("Publish-Subscribe Model Push-Pop")

