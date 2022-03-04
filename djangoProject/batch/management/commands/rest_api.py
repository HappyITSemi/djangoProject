# https://httpbin.org/basic-auth/{user}/{password} basic認証
# HTTPメソッド	エンドポイント
# GET	https://httpbin.org/get
# POST	https://httpbin.org/post
# PATCH	https://httpbin.org/patch
# PUT	https://httpbin.org/put
# DELETE	https://httpbin.org/delete
# https://httpbin.org/status/{codes}

import json
import pprint

import requests as requests
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = '[Usage] python manage.py rest -get get, or -post post'

    def add_arguments(self, parser):
        parser.add_argument('-get', type=str)
        parser.add_argument('-post', type=str)

    def __init__(self, stdout=None, stderr=None, no_color=False, force_color=False):
        super().__init__(stdout, stderr, no_color, force_color)
        self.params = {
            'param1': 'param-val1',
            'param2': 'param-val2'
        }
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': self.get_auth(self),
        }
        self.url_test_post = 'https://httpbin.org/post'
        self.url_test_get = 'https://httpbin.org/get'

    def handle(self, *args, **options):

        if options['get'] == 'get':
            res_get = requests.get(url=self.url_test_get,
                                   params=self.params,
                                   headers=self.headers)

            print('--- get argument--->')
            pprint.pprint(res_get.json())

        elif options['post'] == 'post':
            print('--- post data--->')
            res_post = requests.post(url=self.url_test_post,
                                     json=json.dumps(self.params),
                                     headers=self.headers)

            pprint.pprint(res_post.json())

            print(res_post.json()['json'])
            print('--- post end---')

            print('json=', type(res_post.json()['json']))
            print('headers=', type(res_post.json()['headers']))
