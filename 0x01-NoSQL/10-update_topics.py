#!/usr/bin/env python3
'''updates a mongodb using python function'''


def update_topics(mongo_collection, name, topics):
    '''updates the document for included names'''
    document = mongo_collection.update(
            {name: name},
            {$set: {topics: topics}}
            )
