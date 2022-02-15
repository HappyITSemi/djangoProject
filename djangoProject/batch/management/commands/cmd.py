# HowToUse
# python3 manage.py cmd

import subprocess
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Shell Command exec'

    def handle(self, *args, **options):
        cmd = 'ls -als'

        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        result = proc.communicate()
        (stdout, stderr) = (result[0], result[1])
        print('STDOUT: {}'.format(stdout))
        print('STDERR: {}'.format(stderr))

