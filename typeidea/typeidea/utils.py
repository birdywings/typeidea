# coding:utf-8

from django.core.cache import cache


def cache_it(func):
    def wrapper(self, *args, **kwargs):
        key = repr((func.__name__, args, kwargs))
        if cache.get(key):
            print('hit cache')
            result = cache.get(key)
            return result
        print('hit database')
        result = func(self, *args, **kwargs)
        cache.set(key, result, 60)
        return result
    return wrapper
