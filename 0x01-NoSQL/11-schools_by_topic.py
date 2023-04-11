#!/usr/bin/env python3
"""Python script for mongoDB.
"""


def schools_by_topic(mongo_collection, topic: str):
    """Function that returns list of school by specific topic."""
    filter = {
        "topics": {
            "$elemMatch": {
                "$eq": topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(filter)]
