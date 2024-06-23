#!/usr/bin/env python3
""" Redis client module
"""
import redis
from uuid import uuid4

port = 6380


class Cache:
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: int | bytes | int | float) -> str:
        id = str(uuid4())
        self._redis.set(id, data)
        return id


if "__main__" == __name__:
    cache = Cache()

    data = b"hello"
    key = cache.store(data)
    print(key)

    local_redis = redis.Redis()
    print(local_redis.get(key))
