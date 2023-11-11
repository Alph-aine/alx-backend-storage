#!/usr/bin/env python3
''' list all documents based on a condition'''


def schools_by_topic(mongo_collection, topic):
    '''returns documents with topics'''
    documents =  mongo_collection.find({"topic": topic})
    return list(documents)
