#!/usr/bin/env python3
"""Python script for mongoDB.
"""


def insert_school(mongo_collection, **kwargs):
    """Function that inserts new document in collection."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
