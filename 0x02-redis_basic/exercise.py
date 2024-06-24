#!/usr/bin/env python3
""" Redis client module
"""
import redis
from uuid import uuid4
from typing import Any, Callable, Optional, Union

port = 6379


class Cache:
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        id = str(uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key, fn=None):
        """ Gets key's value from redis and converts
            result byte  into correct data type """
        value = self._redis.get(key)

        if fn is int:
            return self.get_int(value)

        if fn is str:
            return self.get_str(value)

        if callable(fn):
            return fn(value)

        return value

    def get_str(self, data: bytes) -> str:
        """ Converts bytes to string"""
        return data.decode("utf-8")

    def get_int(self, data: bytes) -> int:
        """ Converts bytes to integers """
        return int(data)


if "__main__" == __name__:
    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda data: data.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        print(cache.get(key, fn=fn), value)

        assert cache.get(key, fn=fn) == value
