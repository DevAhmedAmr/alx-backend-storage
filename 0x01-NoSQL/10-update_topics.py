#!/usr/bin/python3
"""Python function that changes all topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    mongo_collection.update({"name": name, "topics": topics}, False, True)
