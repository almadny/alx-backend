#!/usr/bin/python3
""" Module that contains the BasicCache Class"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class Basic Cache """
    def put(self, key, item):
        """ Stores a data in a Cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get a value from cache """
        return self.cache_data.get(key, None)
