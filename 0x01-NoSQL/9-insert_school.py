#!/usr/bin/env python3
'''Insert into a db based on kwargs'''


def insert_school(mongo_collection, **kwargs):
    '''Inserts into the db'''
    document = mongo_collection.insert(kwargs)

    return document
