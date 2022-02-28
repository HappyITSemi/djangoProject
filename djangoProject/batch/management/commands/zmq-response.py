# https://zguide.zeromq.org/
import time
import zmq
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Runs ZMQ server-response'

    def handle(self, *args, **options):
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://*:5555")

        while True:
            #  Wait for next request from client
            message = socket.recv()
            print("【Response】 ----> Received request: %s" % message)

            #  Do some 'work'
            time.sleep(1)

            #  Send reply back to client
            socket.send(b"send World from response")
