#!/usr/bin/python3
""" List all documents in Python

	"""


def list_all(mongo_collection):
    """ List all documents in Python

        Args:
                mongo_collection (Collection): collection to get all it's documents

        Returns:
                dict: all documents
        """
    return mongo_collection.find()
