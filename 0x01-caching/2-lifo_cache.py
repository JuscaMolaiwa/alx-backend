#!/usr/bin/env python3
"""Last-In First-Out (LIFO) caching strategy.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Defines a caching system that stores items,
    with the Last-In, First-Out (LIFO) removal
    policy when the cache limit is exceeded.
    """
    
    def __init__(self):
        """Sets up the LIFO cache instance.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Inserts an item into the cache.
        
        If adding the new item causes the cache to exceed
        the predefined size limit, the most recently added
        item is removed.
        """
        if key is None or item is None:
            return

        # Remove the most recent entry if size limit is reached
        if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key, _ = self.cache_data.popitem(last=True)
            print("DISCARD:", last_key)
        
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Fetches an item by its key from the cache.
        
        Returns None if the key is not present.
        """
        return self.cache_data.get(key, None)
