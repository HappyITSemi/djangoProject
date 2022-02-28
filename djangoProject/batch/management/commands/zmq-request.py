# https://zguide.zeromq.org/

from django.core.management import BaseCommand
import zmq
import logging


class Command(BaseCommand):
    help = '[description] zmq-client-request'

    def handle(self, *args, **options):
        context = zmq.Context()

        #  Socket to talk to server
        print("Connecting to hello world server…")
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:5555")

        #  Do 10 requests, waiting each time for a response
        for request in range(10):
            print("Sending request %s …" % request)
            socket.send(b"send Hello from request")

            #  Get the reply.
            message = socket.recv()
            print("Received reply %s [ %s ]" % (request, message))
