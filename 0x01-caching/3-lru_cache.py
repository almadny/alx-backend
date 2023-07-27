#!/usr/bin/python3
""" Module that contains the BasicCache Class"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Class Basic Cache """

    def __init__(self):
        """Initializes the FIFO Object"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Stores a data in a Cache """

        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                    last_key, value = self.cache_data.popitem(False)
                    print(f"DISCARD: {last_key}")

            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """ Get a value from cache """
        if key in self.cache_data:
            self.cache_data.move_to_end(key, last=True)
        return self.cache_data.get(key, None)
