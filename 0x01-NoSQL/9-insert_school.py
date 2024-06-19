#!/usr/bin/env python3
from pymongo.aggregation import Collection
""" inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection: Collection, **kwargs):
    """ function that inserts a new document in a collection based on kwargs """

    return mongo_collection.insert_one(kwargs).inserted_id
