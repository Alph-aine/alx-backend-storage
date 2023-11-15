#!/usr/bin/env python3
'''Store data in redis and return key'''

import redis
import uuid
from typing import Union


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
