# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
import requests
import redis
from rq import Queue
import time


def cache_it(func):
    def wrapper( *args, **kwargs):
        print('wrapper wrapper wrapper')
        result = func(*args, **kwargs)
        return result
    return wrapper


@cache_it
def test(x, y):
    print(x + y)


def count_words(url, id):
    print(id)
    return len(requests.get(url).text.split())


def get_q():
    redis_conn = redis.Redis()
    return Queue(connection=redis_conn)


class Command(BaseCommand):

    def handle(self, *args, **options):
        q = get_q()
        len_words_1 = q.enqueue(count_words, 'https://www.baidu.com', 1)
        len_words_2 = q.enqueue(count_words, 'https://www.baidu.com', 2)
        len_words_3 = q.enqueue(count_words, 'https://www.baidu.com', 3)
        time.sleep(2)
        print(len_words_1.result)

