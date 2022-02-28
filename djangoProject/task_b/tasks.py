from celery import shared_task


@shared_task
def hello_from_b(*args, **kwargs):
    print("Hello! From A")
    print("args = {}".format(args))
    print("kwargs = {}".format(kwargs))
