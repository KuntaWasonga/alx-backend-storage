#!/usr/bin/env python3
"""Python script for mongoDB.
"""
from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]):
    """Function that changes all topics of document based on name."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
