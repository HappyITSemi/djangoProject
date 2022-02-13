# HowToUse
# https://dev.classmethod.jp/articles/python-subprocess-shell-command/
# python3 manage.py test batchline.management.commands.java_cmd
# python3 manage.py java_cmd

import subprocess
from pathlib import Path

from django.core.management import BaseCommand

BASE_DIR = Path(__file__).resolve().parent.parent


class Command(BaseCommand):
    help = 'Exec Shell Command'
    args = '--version'

    def handle(self, *args, **options):
        _cmd = 'python3 manage.py shell '
        args = "--version > " + str(BASE_DIR) + '/media/outdata/shell_stdout_file.txt'
        cmd = _cmd + args
        print(cmd)

        # java_stdout_file = BASE_DIR + '/media/outdata/java_stdout_file.txt'
        # with open(java_stdout_file, 'w') as stdout_file:
        proc = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # proc = subprocess.run(cmd, shell=True, stdout=java_stdout_file, stderr=subprocess.PIPE, text=True)

        print('STDOUT: {}'.format(proc.stdout))
        print('STDERR: {}'.format(proc.stderr))

        return proc.stderr

        # result = subprocess.run(cmd.split(), shell=True, check=True)
        # return result
