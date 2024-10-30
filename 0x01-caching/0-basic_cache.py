#!/usr/bin/env python3
"""Basic caching system module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Implements a simple caching mechanism that allows
    storing and retrieving items in a dictionary.
    """
    def put(self, key, item):
        """Stores an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Fetches an item by key.
        """
        return self.cache_data.get(key, None)
