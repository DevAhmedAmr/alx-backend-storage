#!/usr/bin/env python3
""" Redis client module
"""
import redis
from uuid import uuid4
from typing import Any, Callable, Optional, Union
from functools import wraps


def replay(method: Callable):
    """ display the history of calls of a particular function.

    Args:
        f (Callable): function

    Returns:
        None: None
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):

        func_name = method.__qualname__
        output_name = func_name + ":outputs"
        input_name = func_name + ":inputs"

        output = self._redis.lrange(output_name, 0, -1)
        input = self._redis.lrange(input_name, 0, -1)
        calls_number = self._redis.get(func_name).decode("utf-8")

        print(func_name + f" was called {calls_number} times")
        for out, inp in zip(output, input):
            out = out.decode('utf-8')
            inp = inp.decode('utf-8')

            print(f"{method.__qualname__}(*{inp}) -> {out}")

    return wrapper


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
    replay_method(cache)


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
