# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand


def cache_it(func):
    def wrapper( *args, **kwargs):
        print('wrapper wrapper wrapper')
        result = func(*args, **kwargs)
        return result
    return wrapper


@cache_it
def test(x, y):
    print(x + y)


class Command(BaseCommand):

    def handle(self, *args, **options):
       test(1, 2)
