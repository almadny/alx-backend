#!/usr/bin/python3
""" Module that contains the BasicCache Class"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """Class Basic Cache """

    def __init__(self):
        """Initializes the FIFO Object"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Stores a data in a Cache """

        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key, value = self.cache_data.popitem(False)
                print(f"DISCARD: {first_key}")

    def get(self, key):
        """ Get a value from cache """
        return self.cache_data.get(key, None)
