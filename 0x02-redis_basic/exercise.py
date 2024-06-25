#!/usr/bin/env python3
""" Redis client module
"""
import redis
from uuid import uuid4
from typing import Any, Callable, Optional, Union
from functools import wraps


def replay(method: Callable) -> None:
    # sourcery skip: use-fstring-for-concatenation, use-fstring-for-formatting
    """
    Replays the history of a function
    Args:
        method: The function to be decorated
    Returns:
        None
    """
    name = method.__qualname__
    cache = redis.Redis()
    calls = cache.get(name).decode("utf-8")
    print("{} was called {} times:".format(name, calls))
    inputs = cache.lrange(name + ":inputs", 0, -1)
    outputs = cache.lrange(name + ":outputs", 0, -1)
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(name, i.decode('utf-8'),
                                     o.decode('utf-8')))


def call_history(method: Callable) -> Callable:
    """
    1- function
    2- wraps returns function
    3- return wraps
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):

        id = method(self, *args, **kwargs)

        self._redis.rpush(f"{method.__qualname__}:outputs", str(id))
        self._redis.rpush(f"{method.__qualname__}:inputs", str(args))
        return id
    return wrapper
    # ---------------------


def count_calls(method: Callable) -> Callable:
    """Increments the count for that key every time the method is
    called and returns the value returned by the original method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """
        class to cash some data

    """

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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
    cache.store("foo")
    cache.store("bar")
    cache.store(42)

    replay_method = replay(cache.store)
