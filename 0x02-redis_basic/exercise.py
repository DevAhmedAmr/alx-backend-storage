#!/usr/bin/env python3
""" Redis client module
"""
import redis
from uuid import uuid4
from typing import Any, Callable, Optional, Union
from functools import wraps


def count_calls(func: callable) -> callable:
    """wrapper that count calls

    Args:
        func (callable): any function

    Returns:
        func
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        key = func.__qualname__
        self._redis.incr(key)
        return func(self, *args, **kwargs)

    return wrapper


class Cache:
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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

    print(cache._redis.keys("*"))
    print(cache.get("Cache.store"))
    cache.store(b"first")

    print(cache.get(cache.store.__qualname__))

    cache.store(b"second")
    cache.store(b"third")
    print(cache.get(cache.store.__qualname__))

# def random_power(x):
#     def f(x):
#         return x**2

#     def g(y):
#         return y**3

#     def h(z):
#         return z**4
#     functions = [f, g, h]
#     return random.choice(functions)(x)

# for i in range(3):
#     p = random_power(i)
#     print(p)
# for i in range(100):
#     x()
