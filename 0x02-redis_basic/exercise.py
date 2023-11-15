#!/usr/bin/env python3
'''Store data in redis and return key'''

import redis
import uuid
from functools import wraps
from typing import Callable, Union


def count_calls(method: Callable) -> Callable:
    '''Tracks the number of times the class is called'''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    '''stores history of inputs and outputs of a function'''
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{key}:inputs"
        output_key = f"{key}:outputs"

        self._redis.rpush(input_key, str(args))
        data = method(self, *args, **kwargs)

        self._redis.rpush(output_key, str(data))
        return data
    return wrapper


class Cache:
    '''cache class'''
    def __init__(self):
        '''Connects and flushes the db'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Generates random key and stores data in redis using key'''
        key = str(uuid.uuid4())

        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Callable = None) -> Union[
            str, bytes, int, None
    ]:
        '''Getter method'''
        data = self._redis.get(key)

        if data is not None and fn is not None:
            return fn(data)

        return data

    def get_str(self, key: str) -> Union[str, None]:
        '''The get str of get'''
        return self.get(key, fn=lambda d: decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        '''The int version of get'''
        return self.get(key, fn=int)
