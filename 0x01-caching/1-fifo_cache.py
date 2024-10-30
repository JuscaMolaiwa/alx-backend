#!/usr/bin/env python3
"""
1. FIFO caching system
"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Implements a caching system that stores items
    using a First-In-First-Out (FIFO) approach when
    the cache reaches its size limit.
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
