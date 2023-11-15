#!/usr/bin/env python3
'''Store data in redis and return key'''

import redis
import uuid
from typing import Callable, Union


class Cache:
    '''cache class'''
    def __init__(self):
        '''Connects and flushes the db'''
        self._redis = redis.Redis()
        self._redis.flushdb()

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
