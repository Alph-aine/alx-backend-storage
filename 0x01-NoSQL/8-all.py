#!/usr/bin/env python3
''' Accessing mongodb from python using pymongo'''


def list_all(mongo_collection):
    '''List all documents'''
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []
    return documents
